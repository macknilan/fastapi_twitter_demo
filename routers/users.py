"""
Router for Users
"""
# python
import json
from pathlib import Path
from typing import List

# Pydantic
from pydantic import SecretStr, EmailStr

# fastpi
from fastapi import APIRouter, status

# Models
from models.users import User

# router
router = APIRouter(prefix="/users", tags=["Users"])

ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent
path_json_files = ROOT_DIR / "json_files/users.json"


@router.get(
    "/",
    response_model=List[User],
    summary="Show all users",
    status_code=status.HTTP_200_OK,
)
async def list_users():
    """
    Service for list all users
    :return: json with the list if basic user information
    user_id: str
    email: email str
    first_name: str
    last_name: str
    birth_date: datetime
    """
    with open(path_json_files, "r", encoding="utf-8") as json_file:
        # Load the data from the file
        data = json.load(json_file)

    return data


@router.get(
    "/{user_id}",
    response_model=User,
    summary="Show a specific user",
    status_code=status.HTTP_200_OK,
)
async def detail_user():
    """
    Service for show detail of user
    :return: {"Show": "user"}
    """
    return {"Show": "user"}


@router.delete(
    "/{user_id}/delete",
    response_model=User,
    summary="Delete a specific user",
    status_code=status.HTTP_200_OK,
)
async def delete_user():
    """
    Service for delete detail tweet
    :return: {"Delete": "user"}
    """
    return {"Delete": "user"}


@router.put(
    "/{user_id}/update",
    response_model=User,
    summary="Update a specific user",
    status_code=status.HTTP_200_OK,
)
async def update_user():
    """
    Service for Update detail tweet
    :return: {"Update": "User"}
    """
    return {"Update": "User"}
