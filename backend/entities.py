from datetime import date, datetime

from pydantic import BaseModel, Field

class Post(BaseModel):
  written: datetime
  post_id: int
  title: str
  text: str

class PostCollection(BaseModel):
  count: int
  posts: list[Post]

class Review(BaseModel):
  group: str
  title: str
  id: int
  rating: int
  text: str

class ReviewCollection(BaseModel):
  count: int
  reviews: list[Review]