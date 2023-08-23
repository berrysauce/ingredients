import uvicorn
from fastapi import FastAPI, Response, status

# local imports
import ingredients


app = FastAPI(
    title="Ingredients – API",
    docs_url=None,
    redoc_url=None
)


@app.get("/")
def get_root():
    return {
        "title": "Ingredients – API",
        "description": "This is the API for the Ingredients web scanner.",
        "license": "github.com/berrysauce/ingredients/blob/master/LICENSE"
    }


@app.get("/scan")
def get_scan(url: str, response: Response):
    try:
        return ingredients.scan(url)
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {
            "error": str(e)
        }


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)