from fastapi import APIRouter

# app = FastAPI()
router = APIRouter()

@router.get("/")
async def welcome():
    return {"message": "Welcome to the FastAPI application!"}