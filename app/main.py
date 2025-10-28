from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import sqlite3
from typing import Optional

app = FastAPI(title="FastAPI Orders Example")

class Order(BaseModel):
    customer_id: int = Field(..., ge=1)
    amount: float = Field(..., gt=0)
    note: Optional[str] = None

DB = "orders.db"

def init_db():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER,
        amount REAL,
        note TEXT
    )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.post("/orders", status_code=201)
async def create_order(order: Order):
    try:
        conn = sqlite3.connect(DB)
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO orders (customer_id, amount, note) VALUES (?, ?, ?)",
            (order.customer_id, order.amount, order.note)
        )
        conn.commit()
        order_id = cur.lastrowid
        conn.close()
        return {"id": order_id, "customer_id": order.customer_id, "amount": order.amount}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
