from typing import Optional

import strawberry


@strawberry.type
class CommentsType:
    id: int
    user_id: int
    post_id: int
    body: str


@strawberry.type
class PostType:
    id: int
    user_id: int
    title: str
    body: str
    comments: Optional[list[CommentsType]]


@strawberry.type
class UserType:
    id: int
    name: str
    address: str
    phone_number: str
    sex: str
    posts: Optional[list[PostType]]
    comments: Optional[list[CommentsType]]


@strawberry.input
class UserInput:
    name: str
    email: str
    address: str
    phone_number: str
    sex: str


@strawberry.input
class PostInput:
    user_id: int
    title: str
    body: str


@strawberry.input
class CommentInput:
    user_id: int
    post_id: int
    body: str
