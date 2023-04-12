from datetime import datetime
from enum import Enum
from typing import List, Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


data_people2 = [
    {"id": 1, "role": "admin", "name": "Charly"},
    {"id": 2, "role": "investor", "name": "Harry"},
    {"id": 3, "role": "trader", "name": "Ken"},
    {"id": 4, "role": "trader", "name": "Homer", "degree": [
        {"id": 1, "created_at": "2020-09-03T15:36:45", "type_dergee": "expert"}
    ]}]


class DegreeType(Enum):
    newbie = "newbie"
    expert = "expert"


class Degree(BaseModel):
    id: int
    created_at: datetime
    type_dergee: DegreeType


class User(BaseModel):
    id: int
    role: str
    name: str
    degree: Optional[List[Degree]] = []


@app.get("/users/{user_id}", response_model=List[User])
async def getUserId(user_id: int):
    return [user for user in data_people2 if user.get("id") == user_id]


@app.get("/trades")
async def getTrades(limit: int, offset: int):
    return data_trades[offset:][:limit]


@app.post("/users/{user_id}")
async def changeUserName(user_id: int, new_name: str):
    current_user = list(filter(lambda user: user.get("id") == user_id, data_people2))[0]
    current_user["name"] = new_name
    return {'status': 200, 'data': current_user}


data_trades = [
    {"id": 1, "user_id": 1, "currency": "BTC", "side": "buy", "price": 123, "amount": 2.12},
    {"id": 2, "user_id": 1, "currency": "BTC", "side": "buy", "price": 125, "amount": 2.12}]


class Trade(BaseModel):
    id: int
    user_id: int
    currency: str
    side: str
    price: float
    amount: int


@app.post("/trades")
async def addNewTrades(trades: List[Trade]):
    data_trades.extend(trades)
    return {'status': 200, 'data': data_trades}