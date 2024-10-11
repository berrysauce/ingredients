import os
import bs4
import json
import httpx
import asyncio
import aiofiles

# ----------------------------------------
# FUNCTIONS
# ----------------------------------------

async def scan(url):
    matching_ingredients = []
    
    def add_ingredient(category: str, ingredient: str):
        if f"{category}/{ingredient}" not in matching_ingredients:
            matching_ingredients.append(f"{category}/{ingredient}")
    
    categories = await aiofiles.os.listdir("ingredients")
    
    if "categories.json" in categories:
        categories.remove("categories.json")
    if ".DS_Store" in categories:
        categories.remove(".DS_Store") # macOS only, improves compatibility
            
    async with httpx.AsyncClient() as client:
        r = await client.get(url, follow_redirects=True)
    
    # other exceptions handled in main.py
    if r.status_code != 200:
        raise httpx.RequestError(f"Invalid Request Status Code ({r.status_code})")
    
    # Run BeautifulSoup in a separate thread to avoid blocking the event loop
    soup = await asyncio.to_thread(bs4.BeautifulSoup, r.text, "html.parser")
    
    headers = r.headers
    
    
    # ----------------------------------------
    # INGREDIENTS SCANNER
    # ----------------------------------------
    
    for category in categories:
        ingredients = await aiofiles.os.listdir(f"ingredients/{category}")
        
        if ".DS_Store" in ingredients:
            ingredients.remove(".DS_Store") # macOS only, improves compatibility
        
        for ingredient in ingredients:
            async with aiofiles.open(f"ingredients/{category}/{ingredient}", "r") as f:
                f_content = await f.read()
                ingredient_data = json.loads(f_content)
            
            # ----- STATS -----
            # increment total scans for each ingredient
            # <PLACEHOLDER>
            # -----------------
            
            for tag_check in ingredient_data["checks"]["tags"]:
                tags = soup.find_all(tag_check["tag"])
                for tag in tags:
                    # check for tag attribute (value is None)
                    if tag_check["value"] is None and tag.get(tag_check["attribute"]) is not None:
                        add_ingredient(category, ingredient)
                            
                    # check for tag content (attribute is not None) with wildcards      
                    elif tag.get(tag_check["attribute"]) is not None and "*" in tag_check["value"]:
                        checks = tag_check["value"].split("*")
                        successful_checks = 0
                        for check in checks:
                            if check in tag.get(tag_check["attribute"]):
                                successful_checks += 1
                            
                        if successful_checks == len(checks):
                            add_ingredient(category, ingredient)
                                    
                    # check for tag content (attribute is not None)
                    elif tag.get(tag_check["attribute"]) is not None and tag_check["value"] in tag.get(tag_check["attribute"]):
                        add_ingredient(category, ingredient)
                            
                    # check for tag content (attribute is None)
                    elif tag_check["attribute"] is None and tag_check["value"] in tag.text:
                        add_ingredient(category, ingredient)
                    
                    # check for <meta name="generator" content="generator name"> tag
                    # to enable this check, set the tag to "meta", the attribute to "generator"
                    elif tag_check["tag"] == "meta" and tag.get("name") == "generator":
                        if tag_check["value"] in tag.get("content"):
                            add_ingredient(category, ingredient)
                            
                    # check for <meta name="platform" content="platform name"> tag
                    # to enable this check, set the tag to "meta", the attribute to "platform"
                    elif tag_check["tag"] == "meta" and tag.get("name") == "platform":
                        if tag_check["value"] in tag.get("content"):
                            add_ingredient(category, ingredient)
                            
            # TODO: Check header capitalization
                            
            for header_check in ingredient_data["checks"]["headers"]:
                # check request header
                if header_check["header"] in headers:
                    if header_check["value"] is None:
                        add_ingredient(category, ingredient)
                    elif header_check["value"] in headers[header_check["header"]]:
                        add_ingredient(category, ingredient)
    
    # ----------------------------------------
            
    return matching_ingredients