import httpx
import pytest

BASE_URL = "http://localhost:8000/api/todos"
ITERATION = 10
INVALID_ID = 2649

@pytest.mark.asyncio
@pytest.mark.parametrize("iteration", range(ITERATION))
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
@pytest.mark.parametrize("iteration", range(ITERATION))
async def test_get_all_todos(iteration):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

@pytest.mark.asyncio
@pytest.mark.parametrize("iteration", range(ITERATION))
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
@pytest.mark.parametrize("iteration", range(ITERATION))
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
@pytest.mark.parametrize("iteration", range(ITERATION))
async def test_delete_todo(iteration):
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{BASE_URL}/{iteration + 1}")
        assert response.status_code == 204

@pytest.mark.asyncio
@pytest.mark.parametrize("iteration", range(ITERATION))
async def test_get_non_existent_todo(iteration):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/{INVALID_ID + iteration }")
        assert response.status_code == 404
        assert response.json() == {
            "detail": f"Todo with id: {INVALID_ID + iteration} not found"
        }

@pytest.mark.asyncio
@pytest.mark.parametrize("iteration", range(ITERATION))
async def test_create_todo_with_invalid_data(iteration):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{BASE_URL}/", json={"completed": False})
        assert response.status_code == 422
        assert "Field required" in response.json()["detail"][0]["msg"]

@pytest.mark.asyncio
@pytest.mark.parametrize("iteration", range(ITERATION))
async def test_get_todo_with_invalid_id(iteration):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/-{iteration}")
        assert response.status_code == 422
        assert "Input should be greater than 0" in response.json()["detail"][0]["msg"]

if __name__ == "__main__":
    pytest.main()
