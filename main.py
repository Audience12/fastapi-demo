from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Demo API", version="1.0.0")

class HelloResponse(BaseModel):
    message: str
    name: str

@app.get("/health")
async def health():
    """Health check endpoint"""
    return {"status": "healthy", "version": "1.0.0"}

@app.get("/api/hello")
async def hello(name: str = "World"):
    """Hello endpoint with optional name parameter"""
    return HelloResponse(message=f"Hello, {name}!", name=name)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
