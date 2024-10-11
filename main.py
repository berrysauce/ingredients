import json
import httpx
import uvicorn
import aiofiles
from typing import Optional
from urllib.parse import urlparse
from fastapi import FastAPI, Response, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

# local imports
import ingredients


app = FastAPI(
    title="Ingredients – API",
    license_info="https://github.com/berrysauce/ingredients/blob/main/LICENSE.md",
    docs_url=None,
    redoc_url=None
)

origins = [
    "https://ingredients.work",
    "https://dev.ingredients.work",
    "https://cdn.ingredients.work"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_class=HTMLResponse)
async def get_root():
    async with aiofiles.open("pages/api.html", "r") as f:
        return HTMLResponse(content=await f.read())
    

@app.get("/docs")
def get_docs():
    return RedirectResponse(url="https://github.com/berrysauce/ingredients/blob/main/README.md#-using-the-api", status_code=301)


@app.get("/ingredients", response_class=JSONResponse)
async def get_scan(url: str, includeCategories: Optional[bool] = False):
    
    # increase compatibility
    if url[:4] != "http":
        # muhahaha! HTTPS for the win!
        url = "https://" + url
    
    # Parse URL and remove port, query, and fragment
    r = urlparse(url)
    parsed_url = r.scheme + "://" + r.netloc.split(":")[0] + r.path
    
    try:        
        data = await ingredients.scan(parsed_url)
        
        matching_ingredients = data
        matching_categories = []
        return_data = {
            "url": url,
            "matching_ingredients": len(matching_ingredients),
            "matches": {}
        }
        
        for ingredient in matching_ingredients:
            if ingredient.split("/")[0] not in matching_categories:
                matching_categories.append(ingredient.split("/")[0])
                return_data["matches"][ingredient.split("/")[0]] = []
                
        for category in matching_categories:
            for ingredient in matching_ingredients:
                if ingredient.split("/")[0] == category:
                    async with aiofiles.open(f"ingredients/{ingredient}", "r") as f:
                        f_content = await f.read()
                        ingredient_data = json.loads(f_content)
                        
                    ingredient_name = ingredient.split("/")[1].replace(".json", "")
                    
                    # ----- STATS -----
                    # increment matching scans for each ingredient
                    # <PLACEHOLDER>
                    # -----------------
                    
                    return_data["matches"][ingredient.split("/")[0]].append(
                        {
                            "id": ingredient_name,
                            "name": ingredient_data["name"],
                            "description": ingredient_data["description"],
                            "icon": ingredient_data["icon"],
                            #"match_percentage": round(((db_ingredient["matching_scans"] + 1) / db_ingredient["total_scans"]) * 100, 1)
                        }
                    )
        
        if includeCategories:
            async with aiofiles.open("ingredients/categories.json", "r") as f:
                f_content = await f.read()
                return_data["categories"] = json.loads(f_content)
                
        return return_data
    except httpx.InvalidURL as e:
        raise HTTPException(status_code=400, detail=str(e))
    except httpx.RequestError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except:
        raise HTTPException(status_code=500, detail=f"Unknown error")
        
        
@app.get("/icon/{icon}")
async def get_icon(icon: str, response: Response):
    # increase compatibility
    if ".png" not in icon:
        icon += ".png"
        
    # parse icon and remove path, query, and fragment
    parsed_icon = icon.lower().split("/")[0].split("?")[0].split("#")[0]
    
    try:
        async with aiofiles.open("./icons/" + parsed_icon, "rb") as f:
            return Response(content=await f.read(), media_type="image/png")
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Icon not found")
    except:
        raise HTTPException(status_code=500, detail="An error occured while fetching the icon")
        


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
