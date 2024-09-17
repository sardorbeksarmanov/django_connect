from pydantic import BaseModel
from typing import Optional


class RegisterSchema(BaseModel):
    username: Optional[str]
    password: Optional[str]
    email: Optional[str]


class LoginSchema(BaseModel):
    username_or_email: Optional[str]
    password: Optional[str]


class ResetPasswordSchema(BaseModel):
    password: Optional[str]
    password2: Optional[str]


class PostCreateSchema(BaseModel):
    caption: Optional[str]
    image_path: Optional[str]


class PostUpdateSchema(BaseModel):
    caption: Optional[str]
    image_path: Optional[str]


class LikeCreateSchema(BaseModel):
    user_id: Optional[str]
    post_id: Optional[str]


class FollowCreateSchema(BaseModel):
    follower_id: Optional[str]
    following_id: Optional[str]


class CommentCreateSchema(BaseModel):
    user_id: Optional[int]
    post_id: Optional[int]
    content: Optional[str]


class CommentUpdateSchema(BaseModel):
    user_id: Optional[int]
    post_id: Optional[int]
    content: Optional[str]
    