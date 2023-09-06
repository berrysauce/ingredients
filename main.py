import json
import httpx
import uvicorn
from deta import Deta
from typing import Optional
from fastapi import FastAPI, Response, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from urllib.parse import urlparse

# local imports
import ingredients


deta = Deta()

db = deta.Base("ingredients-stats")
cache_db = deta.Base("ingredients-cache")

app = FastAPI(
    title="Ingredients – API",
    license_info="https://github.com/berrysauce/ingredients/blob/main/LICENSE.md",
    docs_url=None,
    redoc_url=None
)

origins = [
    "https://ingredients.tech",
    "https://dev.ingredients.tech",
    "https://cdn-api.ingredients.tech"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_class=HTMLResponse)
def get_root():
    with open("pages/api.html", "r") as f:
        return HTMLResponse(content=f.read())
    

@app.get("/docs")
def get_docs():
    return RedirectResponse(url="https://github.com/berrysauce/ingredients/blob/main/README.md#-using-the-api", status_code=301)


@app.get("/ingredients", response_class=JSONResponse)
def get_scan(url: str, includeCategories: Optional[bool] = False):
    
    # Parse URL and remove port, query, and fragment
    r = urlparse(url)
    parsed_url = r.scheme + "://" + r.netloc.split(":")[0] + r.path
    
    # ----- CACHE -----
    # request data from cache
    try:
        cache_data = cache_db.get(key=url)
        if cache_data != None:
            if cache_data["categories"].get("other"):
                # move "other" to the end of the dict
                cache_data["categories"]["other"] = cache_data["categories"].pop("other")
            return cache_data
    except Exception:
        # Deta hasn't defined a specific exception for this error
        # just ignore it
        pass
    # -----------------
    
    try:        
        data = ingredients.scan(parsed_url)
        
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
                    with open(f"ingredients/{ingredient}", "r") as f:
                        ingredient_data = json.loads(f.read())
                        
                    ingredient_name = ingredient.split("/")[1].replace(".json", "")
                        
                    # ----- STATS -----
                    # increment matching scans for each ingredient
                    db_ingredient = db.get(ingredient_name)
                    
                    try:
                        db.update(key=ingredient_name, updates={
                            "matching_scans": int(db_ingredient["matching_scans"]) + 1
                        })
                    except Exception:
                        # Deta hasn't defined a specific exception for this error
                        # just ignore it
                        pass
                    # -----------------
                    
                    return_data["matches"][ingredient.split("/")[0]].append(
                        {
                            "id": ingredient_name,
                            "name": ingredient_data["name"],
                            "description": ingredient_data["description"],
                            "icon": ingredient_data["icon"],
                            "match_percentage": round(((db_ingredient["matching_scans"] + 1) / db_ingredient["total_scans"]) * 100, 1)
                        }
                    )
        
        if includeCategories:
            with open("ingredients/categories.json", "r") as f:
                return_data["categories"] = json.loads(f.read())
        
        # ----- CACHE -----
        # add data to cache
        # expiry: 15 minutes (900 seconds)
        try:
            cache_db.put(key=url, data=return_data, expire_in=900)
        except Exception:
            # Deta hasn't defined a specific exception for this error
            # just ignore it
            pass
        # -----------------
                
        return return_data
    except httpx.InvalidURL as e:
        raise HTTPException(status_code=400, detail=str(e))
    except httpx.RequestError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except:
        raise HTTPException(status_code=500, detail=f"Unknown error")
        
        
@app.get("/icon/{icon}")
def get_icon(icon: str, response: Response):
    # increase compatibility
    if ".png" not in icon:
        icon += ".png"
        
    # parse icon and remove path, query, and fragment
    parsed_icon = icon.lower().split("/")[0].split("?")[0].split("#")[0]
    
    try:
        with open("./icons/" + parsed_icon, "rb") as f:
            return Response(content=f.read(), media_type="image/png")
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Icon not found")
    except:
        raise HTTPException(status_code=500, detail="An error occured while fetching the icon")
        


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
