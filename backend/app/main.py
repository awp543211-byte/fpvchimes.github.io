from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi.responses import JSONResponse
from app.routes import router

limiter = Limiter(key_func=get_remote_address)

app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(
    RateLimitExceeded,
    lambda r, e: JSONResponse(status_code=429, content={"error": "Too many requests"})
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://fpvchimes.github.io"],  # GitHub Pages URL
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

