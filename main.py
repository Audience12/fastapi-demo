from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from typing import Dict

app = FastAPI(title="Demo API", version="1.0.0")

class HelloResponse(BaseModel):
    message: str
    name: str

@app.get("/health")
async def health() -> Dict[str, str]:
    """
    Health check endpoint.
    
    Returns the service status and current timestamp in ISO8601 format.
    This endpoint can be used by load balancers and monitoring systems
    to verify that the API is running correctly.
    
    Returns:
        Dict with 'status' (always 'ok') and ISO8601 formatted 'timestamp'
    """
    return {
        "status": "ok",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }

@app.get("/api/hello")
async def hello(name: str = "World"):
    """Hello endpoint with optional name parameter"""
    return HelloResponse(message=f"Hello, {name}!", name=name)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
