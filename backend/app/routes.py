from fastapi import APIRouter, UploadFile, Form, HTTPException
from fastapi.responses import JSONResponse
from app.database import db
import aiofiles
import os

router = APIRouter()

# Directory to store uploads temporarily
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

ALLOWED_EXTENSIONS = {".mp3", ".midi"}
MAX_FILES_PER_UPLOAD = 1  # Limit 1 per upload for simplicity

@router.post("/songs")
async def upload_song(file: UploadFile, name: str = Form(...)):
    # Check file extension
    ext = os.path.splitext(file.filename)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail="Only .mp3 and .midi allowed")

    # Check name is not empty
    if not name.strip():
        raise HTTPException(status_code=400, detail="Song name is required")

    # Save file temporarily
    temp_path = os.path.join(UPLOAD_DIR, file.filename)
    async with aiofiles.open(temp_path, "wb") as f:
        content = await file.read()
        await f.write(content)

    # Insert into MongoDB safely
    song_doc = {"name": name, "filename": file.filename}
    await db.songs.insert_one(song_doc)

    # Return response
    return JSONResponse({"message": "Song uploaded", "song": song_doc})

@router.get("/songs")
async def list_songs():
    songs = []
    async for s in db.songs.find({}, {"_id": 0}).sort("_id", -1).limit(50):
        songs.append(s)
    return {"songs": songs}
