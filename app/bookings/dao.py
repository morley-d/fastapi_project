from app.database import async_session_maker
from sqlalchemy import select
from app.bookings.models import Bookings


class BookingDAO:

    @classmethod
    async def find_all(cls):
        async with async_session_maker as session:
            query = select(Bookings)
            booking = await session.execute(query)
            return booking.scalars().all()
