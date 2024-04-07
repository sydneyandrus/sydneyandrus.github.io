from datetime import date
from typing import Literal

from fastapi import APIRouter

from backend.entities import (
  Post,
  PostCollection,
)

from backend import database as db

diary_router = APIRouter(prefix="/diary", tags=["Posts"])

@diary_router.get("", response_model=PostCollection)
def get_posts(
  sort: Literal["written"] = "written",
):
  sort_key = lambda post: getattr(post, sort)
  posts = db.get_all_posts()
  return PostCollection(
    count = len(posts),
    posts=sorted(posts, key=sort_key),
  )

@diary_router.get("/{post_id}", response_model=Post)
def get_post(post_id: int):
  return db.get_post_by_id(post_id)