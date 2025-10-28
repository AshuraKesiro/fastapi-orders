# fastapi-orders

Краткое описание: небольшой демонстрационный backend с endpoint POST /orders.
Stack: FastAPI, sqlite (для простоты), pytest (асинхронные тесты).

## Запуск локально
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload

## Тесты
pytest -q

## Docker
docker build -t fastapi-orders .
docker run -p 8000:8000 fastapi-orders
