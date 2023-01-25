"""
Model User
"""

# python
from uuid import UUID, uuid4
from datetime import date

# Pydantic
from pydantic import BaseModel, Field, SecretStr, SecretBytes, EmailStr


class UserBase(BaseModel):
    """
    Model User
    """

    user_id: UUID = Field(
        default_factory=uuid4(), title="ID User", description="ID of the user in UUID"
    )
    email: EmailStr = Field(title="Email", description="User email")


class User(UserBase):
    """
    Model User base of UserBase
    """

    first_name: str = Field(
        title="First name",
        description="First name",
        min_length=6,
        max_length=20,
        example="John Doe",
    )
    last_name: str = Field(
        title="Last name",
        description="Last name",
        min_length=6,
        max_length=20,
        example="Smith",
    )
    birth_date: date | None = Field(
        default=None,
        title="Day of birth",
        description="Day of birth of user",
    )


class PasswordMixin(BaseModel):
    password: str = Field(
        title="Password",
        description="Password user, minimo 8 caracteres, máximo 20 caracteres",
        min_length=8,
        max_length=64,
        example="DkjS/WhH1pVhZ9oLSluR",
    )


class UserLogin(
    PasswordMixin, UserBase
):  # Utilizamos la herencia de clases para añadir password aquí.
    """
    Model login user
    """

    pass


class UserRegister(
    PasswordMixin, User
):  # Utilizamos la herencia de clases para añadir password aquí.
    """
    Model register user
    """

    pass
