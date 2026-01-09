import os
from motor.motor_asyncio import AsyncIOMotorClient

# Read MongoDB URI from environment variable
MONGO_URL = os.getenv("MONGO_URL")

# Add extra options to ensure proper SSL/TLS handshake
client = AsyncIOMotorClient(
    MONGO_URL,
    tls=True,                     # Force TLS
    tlsAllowInvalidCertificates=False,  # Ensure certificates are validated
    serverSelectionTimeoutMS=5000 # Fail fast if connection cannot be made
)

# Get the database (use the one specified in the URI)
db = client.get_default_database()
