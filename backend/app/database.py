from motor.motor_asyncio import AsyncIOMotorClient
from motor.errors import ServerSelectionTimeoutError
import asyncio
from app.config import get_settings

settings = get_settings()

client: AsyncIOMotorClient = None
database = None


async def connect_to_mongodb():
    """Connect to MongoDB with retry logic"""
    global client, database
    
    max_retries = 15
    retry_delay = 3
    
    for attempt in range(max_retries):
        try:
            print(f"MongoDB connect attempt {attempt + 1}/{max_retries}...")
            client = AsyncIOMotorClient(
                settings.mongodb_url,
                serverSelectionTimeoutMS=5000,
                connectTimeoutMS=5000
            )
            database = client[settings.database_name]
            
            # Test connection
            await client.admin.command('ping')
            
            # Create indexes
            await database.users.create_index("username", unique=True)
            await database.portfolios.create_index("username", unique=True)
            
            print(f"✓ Connected to MongoDB: {settings.database_name}")
            return
            
        except ServerSelectionTimeoutError as e:
            print(f"MongoDB not ready (attempt {attempt + 1}): {str(e)[:100]}")
        except Exception as e:
            print(f"MongoDB connect error (attempt {attempt + 1}): {str(e)}")
        
        if attempt < max_retries - 1:
            await asyncio.sleep(retry_delay)
    
    raise Exception(f"Failed to connect to MongoDB after {max_retries} attempts")


async def close_mongodb_connection():
    """Close MongoDB connection"""
    global client
    if client:
        client.close()
        print("MongoDB connection closed")


def get_database():
    """Get database instance"""
    return database

