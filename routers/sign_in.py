"""
Router for Sign In
"""

# Pydantic
from pydantic import SecretStr, EmailStr

# fastpi
from fastapi import APIRouter, status, Form

# Models

router = APIRouter(tags=["Sign In"])


# Data Forms
@router.post(
    "/sign-in",
    # response_model=LoginOut,
    response_model_exclude={"password"},
    status_code=status.HTTP_200_OK,
    summary="Sing In"
)
async def sign_in(username: str = Form(), password: SecretStr = Form()):
    """
    Servicio para Sign In por medio de data form

    :param username:
    :param password:
    :return: { "username": "werouwoeriu",  "message": "Login successful (͠≖ ͜ʖ͠≖)👌"}
    """
    # return LoginOut(username=username)
    return {"username": username}


@router.post(
    "/sign-up",
    # response_model=LoginOut,
    response_model_exclude={"password"},
    status_code=status.HTTP_200_OK,
    summary="Sing Up"
)
async def sign_up(username: str = Form(), email: EmailStr = Form(), password: SecretStr = Form()):
    """
    Servicio para Sign Up por medio de data form

    :param username:
    :param email:
    :param password:
    :return: { "username": "werouwoeriu",  "message": "Login successful (͠≖ ͜ʖ͠≖)👌"}
    """
    # return LoginOut(username=username)
    return {"username": username}
