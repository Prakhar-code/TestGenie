# main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field
from typing import List
from constant import users

app = FastAPI()


@app.get("/")
async def root():
    return {"messsage": "Hello World"}


class User(BaseModel):
    name: str = Field(..., min_length=1)
    email: EmailStr
    employee_id: str = Field(..., min_length=1)
    password: str = Field(..., min_length=6)
    confirm_password: str = Field(..., min_length=6)


class UserResponse(BaseModel):
    name: str = Field(..., min_length=1)
    email: EmailStr
    employee_id: str = Field(..., min_length=1)
    password: str = Field(..., min_length=6)


@app.post("/user/register", response_model=UserResponse)
async def register_user(user: User):

    # Check if passwords match
    if user.password != user.confirm_password:
        raise HTTPException(status_code=404, detail="Passwords do not match")

    # Check if user already exists
    for existing_user in users:
        if existing_user["email"] == user.email:
            raise HTTPException(status_code=404, detail="Email already registered")

    # Create a new user
    new_user = user.dict(
        exclude={"confirm_password"}
    )  # Exclude confirm_password from the stored data
    users.append(new_user)  # Store user data in the constant list

    response = UserResponse(
        name=user.name,
        email=user.email,
        employee_id=user.employee_id,
        password=user.password,
    )

    return response
