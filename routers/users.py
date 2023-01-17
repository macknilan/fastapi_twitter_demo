"""
Router for Users
"""

# Pydantic
from pydantic import SecretStr, EmailStr

# fastpi
from fastapi import APIRouter, status

# Models

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", summary="Show all users", status_code=status.HTTP_200_OK)
async def list_users():
    """
    Service for list all users
    :return: {"Users": "All"}
    """
    return {"Users": "All"}


@router.get("/{user_id}", summary="Show a specific user", status_code=status.HTTP_200_OK)
async def detail_user():
    """
    Service for show detail of user
    :return: {"Show": "user"}
    """
    return {"Show": "user"}


@router.delete("/{user_id}/delete", summary="Delete a specific user", status_code=status.HTTP_200_OK)
async def delete_user():
    """
    Service for delete detail tweet
    :return: {"Delete": "user"}
    """
    return {"Delete": "user"}


@router.put("/{user_id}/update", summary="Update a specific user", status_code=status.HTTP_200_OK)
async def update_user():
    """
    Service for Update detail tweet
    :return: {"Update": "User"}
    """
    return {"Update": "User"}
