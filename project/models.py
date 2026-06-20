from datetime import datetime
from sqlmodel import SQLModel, Field
from sqlalchemy import Index

class UserBase(SQLModel):
    email: str = Field(unique=True)

class UserRead(UserBase):
    premium: bool

class UserCreate(UserBase):
    password: str
class Users(UserCreate, table=True):
    id: int | None = Field(default=None, primary_key=True)
    premium: bool = Field(default=False)

class CreateTarget(SQLModel):
    name: str | None = None
    description: str | None = None
    url: str
class Target(CreateTarget, table=True):
    __table_args__ = (
        Index('start_check', 'is_active', 'next_check'),
    )
    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key='users.id')
    is_active: bool = Field(default=True)
    next_check: datetime = Field(default_factory=datetime.now)

class Result(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key='users.id')
    target: int = Field(foreign_key='target.id',index=True)
    is_up: bool | None = None
    status_code: str | None = None
    response_speed: float | None = None
    checked_at: datetime = Field(default_factory=datetime.now)