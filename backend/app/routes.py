from fastapi import APIRouter
from app.database import songs
from app.models import Song

router = APIRouter()

@router.post("/songs")
async def upload_song(song: Song):
    await songs.insert_one(song.dict())
    return {"ok": True}

@router.get("/songs")
async def list_songs():
    data = []
    async for s in songs.find({}, {"_id": 0}).sort("_id", -1).limit(50):
        data.append(s)
    return data

@router.post("/songs/{song_name}/like")
async def like_song(song_name: str):
    res = await songs.update_one({"name": song_name}, {"$inc": {"likes": 1}})
    if res.matched_count == 0:
        return {"error": "Song not found"}
    return {"ok": True}
