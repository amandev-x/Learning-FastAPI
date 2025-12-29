from fastapi import FastAPI
from todo import todo_router

app = FastAPI()

"""
Incuded include_router().
Both FastAPI and APIRouter works in same way but uvicorn cannot use APIRouter instance to server the application.
It uses FastAPI to serve the applicatio
But why include_route()?
This is responsible for adding routes defined in the APIRouter class in the project to the main application
"""
app.include_router(todo_router)

@app.get("/")
async def welcome():
    return {"message": "Welcome to the FastAPI application!"}

