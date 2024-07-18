from datetime import datetime
from enum import Enum
from typing import Annotated, Optional
from pydantic import BaseModel, BeforeValidator, Field

# Represents an ObjectId field in the database
# It will be represented as a `str` on the model so that it can be serialized to JSON.
PyObjectId = Annotated[str, BeforeValidator(str)] 

class Task(BaseModel):
    """
    The user model
    """
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    # user_id: PyObjectId | None = None
    title: str | None = None
    description: str | None = None
    status: str = "pending"
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None