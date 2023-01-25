"""
Script de FastAPI testing Twitter API
In Python 3.10.6
Run:
    uvicorn main:app --reload
"""

# python
from typing import List
import json
from pathlib import Path

# fastpi
from fastapi import FastAPI, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

# models
from models.tweet import Tweet

# Routes
from routers import tweets, sign_in, users

ROOT_DIR = Path(__file__).resolve(strict=True).parent
path_tweets_json_files = ROOT_DIR / "json_files/tweets.json"


app = FastAPI(
    # root_path="/api/v1",
    openapi_url="/api/v1/openapi.json",
    title="API Twitter testing 🐦",
    version="0.0.1",
    description="Testing routes like Twitter",
    contact={"name": "mack", "url": "http://mack.host"},
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)


@app.get(
    "/",
    response_model=List[Tweet],
    summary="Show all tweets",
    tags=["Twitter"],
    status_code=status.HTTP_200_OK,
)
async def home():
    """
    Show all tweets.

    :return:

        [
            {
                "tweet_id": uuid4,
                "content": str
                "created": datetime,
                "modified": datetime,
                "by": {
                    "user_id": uuid4,
                    "email": str,
                    "first_name": str,
                    "last_name": str,
                    "birth_date": date
                    }
            }
        ]
    """
    with open(path_tweets_json_files, "r", encoding="utf-8") as json_file:
        # Load the data from the file
        data = json.load(json_file)
        json_compatible_tweet_data = jsonable_encoder(data)

        return JSONResponse(content=json_compatible_tweet_data)


app.include_router(sign_in.router)
app.include_router(tweets.router)
app.include_router(users.router)
