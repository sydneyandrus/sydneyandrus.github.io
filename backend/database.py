import json
from datetime import datetime
from uuid import uuid4

from backend.entities import (
  Post,
  PostCollection,
  Review,
  ReviewCollection,
)

with open("backend/db.json", "r") as f:
  DB = json.load(f)

class EntityNotFoundException(Exception):
  def __init__(self, *, entity_name: str, entity_id: str):
    self.entity_name = entity_name
    self.entity_id = entity_id

class RequestValidationException(Exception):
  def __init__(self, *, entity_name: str, entity_id: str):
    self.entity_name = entity_name
    self.entity_id = entity_id

def get_all_posts() -> list[Post]:
  all_posts = []
  for post_data in DB["posts"].values():
    currentPost = Post(
      written = post_data["written"],
      post_id = post_data["post_id"],
      title = post_data["title"],
      text= post_data["text"],
    )
    all_posts.append(currentPost)

  return all_posts

def get_post_by_id(post_id: int) -> Post:
  if post_id in DB["posts"]:
    return Post(**DB["posts"][post_id])
  
def get_all_reviews() -> list[Review]:
  all_reviews = []
  for review_data in DB["reviwes"].values():
    currentReview = Review(
      group = review_data["group"],
      title = review_data["title"],
      id = review_data["id"],
      rating = review_data["rating"],
      text = review_data["text"],
    )
    all_reviews.append(currentReview)

  return all_reviews

def get_reviews_by_id(id: int) -> Review:
  if id in DB["reviews"]:
    return Review(**DB["reviews"][id])

def get_all_reviews_by_group(review_group: str) -> list[Review]:
  reviews = []
  for review_data in DB["reviwes"].values():
    currentReview = Review(
      group = review_data["group"],
      title = review_data["title"],
      id = review_data["id"],
      rating = review_data["rating"],
      text = review_data["text"],
    )
    if currentReview.group is review_group:
      reviews.append(currentReview)

  return reviews