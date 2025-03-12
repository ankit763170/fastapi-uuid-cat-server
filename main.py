from fastapi import FastAPI, Response, HTTPException
import uuid
import asyncio
import httpx

app = FastAPI()

@app.get("/uuid")
def get_uuid():
    """Generate and return a unique version 4 UUID."""
    return {"uuid": str(uuid.uuid4())}

@app.get("/async-uuid")
async def get_async_uuid():
    """
    Generate and return a unique version 4 UUID.
    Ensure the response takes at least 3 seconds (non-blocking).
    """
    await asyncio.sleep(3)
    return {"uuid": str(uuid.uuid4())}

@app.get("/cat")
async def get_cat():
    """
    Fetch a random cat image from https://cataas.com/cat
    and return the image content.
    """
    url = "https://cataas.com/cat"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Failed to fetch cat image")
        content_type = response.headers.get("content-type", "image/jpeg")
        return Response(content=response.content, media_type=content_type)
