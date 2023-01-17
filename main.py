"""
Script de FastAPI testing Twitter API
In Python 3.10.6
Run:
    uvicorn main:app --reload
"""

# fastpi
from fastapi import FastAPI, status

# Routes
from routers import tweets, sign_in, users

app = FastAPI(
    # root_path="/api/v1",
    openapi_url="/api/v1/openapi.json",
    title="API Twitter testing",
    version="0.0.1",
    description="Testing routes like Twitter",
    contact={"name": "mack", "url": "http://mack.host"},
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)


@app.get("/", summary="Show all tweets", tags=["Twitter 🐦"], status_code=status.HTTP_200_OK)
async def all_tweets():
    """
    Service for show all tweets
    :return: {"Show all": "Twits"}
    """
    return {"Show all": "Tweets"}

app.include_router(tweets.router)
app.include_router(sign_in.router)
app.include_router(users.router)
