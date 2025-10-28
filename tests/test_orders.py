import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_create_order():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        payload = {"customer_id": 1, "amount": 10.5, "note": "test"}
        resp = await ac.post("/orders", json=payload)
        assert resp.status_code == 201
        data = resp.json()
        assert "id" in data
        assert data["customer_id"] == 1
