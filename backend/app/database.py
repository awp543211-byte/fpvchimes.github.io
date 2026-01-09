import os
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = os.environ["MONGO_URL"]

client = AsyncIOMotorClient(MONGO_URL)
db = client.bluejay
songs = db.songs
