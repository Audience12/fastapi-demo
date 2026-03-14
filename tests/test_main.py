import sys
sys.path.insert(0, '.')
import pytest
from httpx import AsyncClient
from main import app

@pytest.fixture
def anyio_backend():
    return "asyncio"

@pytest.mark.anyio
async def test_health():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["version"] == "1.0.0"

@pytest.mark.anyio
async def test_hello_default():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/api/hello")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Hello, World!"
    assert data["name"] == "World"

@pytest.mark.anyio
async def test_hello_with_name():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/api/hello?name=Claude")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Hello, Claude!"
    assert data["name"] == "Claude"
