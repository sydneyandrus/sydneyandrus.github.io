from datetime import date
from typing import Literal

from fastapi import APIRouter

from backend.entities import (
  Review,
  ReviewCollection,
)

from backend import database as db

library_router = APIRouter(prefix="/library", tags=["Reviews"])

@library_router.get("/columbo", response_model=ReviewCollection)
def get_columbo_reviews():
  reviews = db.get_all_reviews_by_group("columbo")
  return ReviewCollection(
    count = len(reviews),
    reviews=reviews,
  )

@library_router.get("/bookshelf", response_model=ReviewCollection)
def get_book_reviews():
  reviews = db.get_all_reviews_by_group("book")
  return ReviewCollection(
    count = len(reviews),
    reviews=reviews,
  )

@library_router.get("/columbo/{id}", response_model=Review)
def get_review(id: int):
  return db.get_reviews_by_id(id)