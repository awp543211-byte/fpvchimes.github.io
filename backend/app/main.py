from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router as songs_router  # your songs routes

app = FastAPI()

# CORS configuration
origins = [
    "https://awp543211-byte.github.io/fpvchimes.github.io",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)

# Include your routes
app.include_router(songs_router)

