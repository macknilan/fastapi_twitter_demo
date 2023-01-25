"""
Model Tweet
"""

# python
from enum import Enum
from uuid import UUID, uuid4
from datetime import date, datetime

# Pydantic
from pydantic import BaseModel, Field

# Models
from models.users import User


class Tweet(BaseModel):
    """
    Tweet model
    """

    tweet_id: UUID = Field(
        default_factory=uuid4(), title="ID User", description="ID of the user in UUID"
    )
    content: str = Field(
        title="Tweet content",
        description="Content of the Tweet",
        min_length=6,
        max_length=256,
        example="Lorem ipsum dolor sit amet",
    )
    created: datetime = Field(
        title="created at",
        description="Date time on which the object was created.",
        default=datetime.now(),
    )
    modified: datetime | None = Field(
        default=None,
        title="modified at",
        description="Date time on which the object was last modified.",
    )
    by: User = Field(title="Tweet by", description="Who is the owner of the tweet")
