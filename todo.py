from fastapi import APIRouter
todo_router = APIRouter()

# Create Temporary in-app database alongside two routes for the additional and retrieval of todo items.
todo_list = []

# Create a POST method to add a todo item in the todo_list
@todo_router.post("/todo")
async def add_todo(todo):
    todo_list.append(todo)
    return {"Message": "Todo item has been added successfully."}

# Create a GET method to retrieve all items from the todo_list
@todo_router.get("/todos")
async def get_todos():
    return todo_list

