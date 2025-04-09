import httpx
import pytest

BASE_URL = "http://localhost:8000/api/todos"

@pytest.mark.asyncio
@pytest.mark.parametrize("iteration", range(5))
async def test_create_todo(iteration):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{BASE_URL}/", json={"title": "Buy groceries", "completed": False})
        assert response.status_code == 201
        assert response.json() == {
            "id": iteration + 1, 
            "title": "Buy groceries",
            "completed": False
        }

@pytest.mark.asyncio
@pytest.mark.parametrize("iteration", range(5))
async def test_get_all_todos(iteration):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

@pytest.mark.asyncio
@pytest.mark.parametrize("iteration", range(5))
async def test_get_todo_by_id(iteration):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/{iteration + 1}")
        assert response.status_code == 200
        assert response.json() == {
            "id": iteration + 1,
            "title": "Buy groceries",
            "completed": False
        }

@pytest.mark.asyncio
@pytest.mark.parametrize("iteration", range(5))
async def test_update_todo(iteration):
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{BASE_URL}/{iteration + 1}", json={"title": "Buy groceries and cook dinner", "completed": True})
        assert response.status_code == 200
        assert response.json() == {
            "id": iteration + 1,
            "title": "Buy groceries and cook dinner",
            "completed": True
        }

@pytest.mark.asyncio
@pytest.mark.parametrize("iteration", range(5))
async def test_delete_todo(iteration):
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{BASE_URL}/{iteration + 1}")
        assert response.status_code == 204

@pytest.mark.asyncio
async def test_get_non_existent_todo():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/999")
        assert response.status_code == 404
        assert response.json() == {
            "detail": "Todo with id: 999 not found"
        }

@pytest.mark.asyncio
async def test_create_todo_with_invalid_data():
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{BASE_URL}/", json={"completed": False})
        assert response.status_code == 422
        assert "Field required" in response.json()["detail"][0]["msg"]

@pytest.mark.asyncio
async def test_get_todo_with_invalid_id():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/-8")
        assert response.status_code == 422
        assert "Input should be greater than 0" in response.json()["detail"][0]["msg"]

if __name__ == "__main__":
    pytest.main()
