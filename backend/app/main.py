from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router as songs_router  # your songs routes

app = FastAPI()

# CORS configuration
origins = [
    "https://fpvchimes.github.io",          # your GitHub Pages URL
    "http://localhost:5500",                # optional for local dev
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],   # Allow GET, POST, OPTIONS
    allow_headers=["*"],   # Allow all headers
)

# Include your routes
app.include_router(songs_router)
