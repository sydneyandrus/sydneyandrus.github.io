from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from backend.routers.diary import diary_router
from backend.routers.library import library_router
from backend.database import EntityNotFoundException
from backend.database import RequestValidationException

app = FastAPI(
  title="pony express API",
  description="API for managing chats between users.",
  version="0.1.0",
)

app.include_router(diary_router)
app.include_router(library_router)

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

@app.exception_handler(EntityNotFoundException)
def handle_entity_not_found(
  _request: Request,
  exception: EntityNotFoundException,
) -> JSONResponse:
  return JSONResponse(
    status_code=404,
    content={
      "detail": {
        "type": "entity_not_found",
        "entity_name": exception.entity_name,
        "entity_id": exception.entity_id,
      },
    },
  )

@app.exception_handler(RequestValidationException)
def handle_duplicate_entity(
  _request: Request,
  exception: RequestValidationException,
) -> JSONResponse:
  return JSONResponse(
    status_code=422,
    content={
      "detail": {
        "type": "duplicate_entity",
        "entity_name": exception.entity_name,
        "entity_id": exception.entity_id,
      },
    },
  )

@app.get("/", include_in_schema=False)
def root(): 
	return {"message": "welcome to my blog"}
