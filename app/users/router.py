from fastapi import APIRouter
from app.users.dao import UsersDAO
from app.users.shemas import ShemaUserRegister


router = APIRouter(
    prefix="/auth",
    tags=["Auth & Пользователи"]
)


@router.post("/register")
async def register_user(user_data: ShemaUserRegister):
    existing_user = await UsersDAO.find_one_or_none
