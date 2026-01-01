from pydantic import BaseModel
from typing import List

"""
What is Model in FastAPI?
=> A model is a class that defines the structure of the data that will be sent to the API. It is used to validate the data that is sent to the API.

What is Pydantic Mode?
=> Pydantic is a library in python that is used to validate the data that is sent to the API. It is used to define the structure of the data that will be sent
to the API. Is is used to validate the data that is sent to the API.

"""

class Todo(BaseModel):
    id: int 
    title: str 
    description: str 
    completed: bool = False

    # Using Config class to add example to the model
    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "Buy groceries",
                "description": "Demo for buying groceries",
                "completed": False
            }
        }

"""
Here we are creating a response model for the book product. With the help of this model, we can define the structure of the 
response that will be sent to the client. By using this model FastAPI can validate the response automatically.
This is a best practice to follow and also used in Production level APIs.
In this model, we will return everything except the id of the todo item but we can return the id if we want to.
"""
class TodoResponse(BaseModel):
    title: str 
    description: str 
    completed: bool 
    
    class Config:
        json_schema_extra = {
            "example": {
                "title": "Buy PS5",
                "description": "Demo for buying PS5",
                "completed": False 
            }
        }
    # todo: Todo

"""
Here we are creating another response model to return the list of books. This is also a best practice to follow and also used 
in Production level APIs. The reason behind creating this model is to define the structure of the response that will be sent 
to the client.
"""
class TodoResponseList(BaseModel):
    todos: List[TodoResponse]

    class Config:
        json_schema_extra = {
            "example": {
                "todos": [
                    {
                        "title": "Buy PS5",
                        "description": "Demo for buying PS5",
                        "completed": False 
                    },
                    {
                          "title": "Buy XBOX",
                          "description": "Demo for buying XBOX",
                          "completed": True 
                    }
                ]
            }
        }


class TodoItem(BaseModel):
    title: str
    description: str 
    completed: bool = False

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Buy groceries",
                "description": "Demo for buying groceries",
                "completed": False 
            }
        }
