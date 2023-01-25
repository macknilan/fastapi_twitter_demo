"""
Router for Sign In
"""

# python
import json
from pathlib import Path
from uuid import uuid4

# Pydantic
from pydantic import SecretStr, EmailStr

# fastpi
from fastapi import APIRouter, status, Form, Body

# Models
from models.users import User, UserRegister

# routers
router = APIRouter(prefix="/auth", tags=["Auth"])

ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent
path_users_json_files = ROOT_DIR / "json_files/users.json"


# Data Forms
@router.post(
    "/sign-in", response_model=User, status_code=status.HTTP_200_OK, summary="Sing In"
)
async def sign_in(username: str = Form(), password: SecretStr = Form()):
    """
    Servicio para Sign In por medio de data form

    :param username:
    :param password:
    :return: { "username": "werouwoeriu",  "message": "Sign In successful (͠≖ ͜ʖ͠≖)👌"}
    """

    return {"username": username}


@router.post(
    "/sign-up",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Sing Up",
)
async def sign_up(user: UserRegister = Body(embed=True)):
    """
    Servicio para Sign Up por medio de data form

    :param user: Request ody parameter

        {
          "user": {
            "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "email": "user@example.com",
            "first_name": "John Doe",
            "last_name": "Smith",
            "birth_date": "2023-01-24",
            "password": "DkjS/WhH1pVhZ9oLSluR"
          }
        }
    :return: json with the basic user information

        user_id: str
        email: email str
        first_name: str
        last_name: str
        birth_date: datetime
    """
    with open(path_users_json_files, "r+", encoding="utf-8") as json_file:
        # Load the data from the file
        data = json.load(json_file)
        user_dict = user.dict()
        user_dict["user_id"] = str(uuid4())
        user_dict["birth_date"] = str(user_dict["birth_date"])
        data.append(user_dict)
        # Move the pointer to the beginning of the file
        json_file.seek(0)
        # Write the modified data to the file
        json.dump(data, json_file, indent=4)
        # Truncate the file to the size of the written data
        json_file.truncate()

    return user
