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
    try:
        # Check if the todo_list is empty or not
        if len(todo_list) == 0:
         return {"Message": "Todo list is empty. Please add a item to see the todo lists"}
        else:
           return todo_list
    except Exception as e:
       return f"{e}"

