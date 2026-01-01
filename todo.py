from fastapi import APIRouter, Path, HTTPException
from models import Todo, TodoResponse, TodoResponseList, TodoItem
todo_router = APIRouter()

# Create Temporary in-app database alongside two routes for the additional and retrieval of todo items.
todo_list = []

# Create a POST method to add a todo item in the todo_list
@todo_router.post("/todo")
async def add_todo(todo: Todo) -> dict:
    for existing_todo in todo_list:
        if existing_todo.id == todo.id:
            raise HTTPException(
                status_code=400,
                detail=f"Todo item with id {todo.id} already exists."
            )
    todo_list.append(todo)
    return {"Message": "Todo item has been added successfully."}


# Create a GET method to retrieve all items from the todo_list
# Not using dict beacause we are using response_model to define the response structure
@todo_router.get("/todos", response_model=TodoResponseList)
async def get_todos():
    if len(todo_list) == 0:
        raise HTTPException(
            status_code=404,
            detail="Todo list is empty. Please add a item to see the todo lists"
        )
    else:
        return {"todos": todo_list}
    
"""
Create a GET method to retrieve a specific todo item by its id.
In this method, we are using Path to validate the todo_id parameter. In simple words, we are adding some additional
validation to the todo_id parameter.
This adds better documentation and validation to the Swagger UI and Redoc documentation.
In Path(...), ... means that this parameter is required.
"""
@todo_router.get("/todo/{todo_id}", response_model=TodoResponse)
async def get_todo_by_id(todo_id: int = Path(..., description="The ID of the todo item to retrieve", gt=0, example=1)):
    for todo in todo_list:
        if todo.id == todo_id:
            return {"todo": todo}
       
    # If the item didnt found then raise HTTPException error
    raise HTTPException(
       status_code=404,
       detail="Todo item not found"
       )


"""
Create a PUT method to update a specific todo item by its id.
"""

@todo_router.put("/todo/{todo_id}", response_model=TodoResponse)
async def update_todo_by_id(
    todo_data: TodoItem, todo_id: int = Path(..., description="The ID of the todo item to update", gt=0, example=1)
    ):
    for index, todo in enumerate(todo_list):
        if todo.id == todo_id:
            todo_list[index].title = todo_data.title
            todo_list[index].description = todo_data.description
            todo_list[index].completed = todo_data.completed 
            return {"todo": todo_list[index]}
        
    # If the item didnt found then raise HTTPException error
    raise HTTPException(
        status_code=404,
        detail="Todo item not found"
    )