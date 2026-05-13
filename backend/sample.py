from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field

app = FastAPI()

class UserCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

fake_users = {}
next_id = 1

@app.post("/users", response_model=UserResponse, status_code=201)
async def create_user(user: UserCreate):
    global next_id
    new_user = {"id": next_id, "name": user.name, "email": user.email}
    fake_users[next_id] = new_user
    next_id += 1
    return new_user

@app.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):
    user = fake_users.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put("/users/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user: UserCreate):
    if user_id not in fake_users:
        raise HTTPException(status_code=404, detail="User not found")
    fake_users[user_id].update({"name": user.name, "email": user.email})
    return fake_users[user_id]