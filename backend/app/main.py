# main.py (or app/main.py)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router as songs_router

app = FastAPI()

# Add CORS middleware
origins = [
    "https://awp543211-byte.github.io",   # your GitHub Pages frontend
    "http://localhost:5500",              # optional for local dev
    "https://fpvchimes.github.io",       # alternative frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],   # allow GET, POST, OPTIONS, etc.
    allow_headers=["*"],   # allow custom headers
)

# Include your routes
app.include_router(songs_router)
