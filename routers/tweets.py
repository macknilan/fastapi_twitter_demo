"""
Routes for the Tweets
"""

# FastAPI
from fastapi import APIRouter, status


router = APIRouter(prefix="/tweets", tags=["Tweets"])


@router.post("/", summary="Create tweet", status_code=status.HTTP_200_OK)
async def create_tweet():
    """
    Service for create tweet
    :return: {"Create": "Tweet"}
    """
    return {"Create": "Tweet"}


@router.get("/{tweet_id}", summary="Show a specific tweet", status_code=status.HTTP_200_OK)
async def detail_tweet():
    """
    Service for show detail tweet
    :return: {"Show": "Tweet"}
    """
    return {"Show": "Tweet"}


@router.delete("/{tweet_id}/delete", summary="Delete a specific tweet", status_code=status.HTTP_200_OK)
async def delete_tweet():
    """
    Service for delete detail tweet
    :return: {"Delete": "Tweet"}
    """
    return {"Delete": "Tweet"}


@router.put("/{tweet_id}/update", summary="Update a specific tweet", status_code=status.HTTP_200_OK)
async def update_tweet():
    """
    Service for Update detail tweet
    :return: {"Update": "Tweet"}
    """
    return {"Update": "Tweet"}

