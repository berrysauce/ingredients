import uvicorn
from fastapi import FastAPI, Response, status
from fastapi.responses import JSONResponse, HTMLResponse

# local imports
import api.ingredients as ingredients


app = FastAPI(
    title="Ingredients – API",
    docs_url=None,
    redoc_url=None
)


@app.get("/", response_class=HTMLResponse)
def get_root():
    with open("pages/api.html", "r") as f:
        return HTMLResponse(content=f.read())


@app.get("/scan", response_class=JSONResponse)
def get_scan(url: str, response: Response):
    try:
        data = ingredients.scan(url)
        return data
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {
            "error": str(e)
        }
        
        
@app.get("/icon/{icon}")
def get_icon(icon: str, response: Response):
    try:
        with open("icons/" + icon, "rb") as f:
            return Response(content=f.read(), media_type="image/png")
    except FileNotFoundError:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {
            "error": "Icon not found"
        }
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {
            "error": str(e)
        }
        


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)