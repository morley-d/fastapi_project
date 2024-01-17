from fastapi import APIRouter
from sqlalchemy import select
from app.bookings.dao import BookingDAO
from app.database import async_session_maker
from app.bookings.models import Bookings


router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"]
)


@router.get("")
async def get_bookings():
    async with async_session_maker() as session:
        return await BookingDAO.find_all()


@router.get("/{booking_id}")
def get_booking(booking_id):
    pass
