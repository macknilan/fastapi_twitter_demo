"""
Routes for the Tweets
"""

# python
import json
from pathlib import Path


# FastAPI
from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

# Models
from models.tweet import Tweet

# router
router = APIRouter(prefix="/tweets", tags=["Tweets"])

ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent
path_tweets_json_files = ROOT_DIR / "json_files/tweets.json"


@router.post(
    "/",
    response_model=Tweet,
    summary="Create tweet",
    status_code=status.HTTP_201_CREATED,
)
async def create_tweet(tweet: Tweet):
    """
    Create tweet

    :param: tweet

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
    with open(path_tweets_json_files, "r+", encoding="utf-8") as json_file:
        # Load the data from the file
        data = json.load(json_file)
        json_compatible_tweet_data = jsonable_encoder(tweet)
        data.append(json_compatible_tweet_data)
        # Move the pointer to the beginning of the file
        json_file.seek(0)

        # Write the modified data to the file
        json.dump(data, json_file, indent=4)

        # Truncate the file to the size of the written data
        json_file.truncate()

        return JSONResponse(content=data)


@router.get(
    "/{tweet_id}",
    response_model=Tweet,
    summary="Show a specific tweet",
    status_code=status.HTTP_200_OK,
)
async def detail_tweet():
    """
    Service for show detail tweet
    :return: {"Show": "Tweet"}
    """
    return {"Show": "Tweet"}


@router.delete(
    "/{tweet_id}/delete",
    response_model=Tweet,
    summary="Delete a specific tweet",
    status_code=status.HTTP_200_OK,
)
async def delete_tweet():
    """
    Service for delete detail tweet
    :return: {"Delete": "Tweet"}
    """
    return {"Delete": "Tweet"}


@router.put(
    "/{tweet_id}/update",
    response_model=Tweet,
    summary="Update a specific tweet",
    status_code=status.HTTP_200_OK,
)
async def update_tweet():
    """
    Service for Update detail tweet
    :return: {"Update": "Tweet"}
    """
    return {"Update": "Tweet"}
