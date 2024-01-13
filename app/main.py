from fastapi import FastAPI, Query, Depends
from typing import Optional
from datetime import date
from pydantic import BaseModel


app = FastAPI()


class ShemaHotel(BaseModel):
    adress: str
    name: str
    stars: int



@app.get("/hotels/")
def get_hotels(
    search_args: HotelSearchArgs = Depends()
):
    hotels = [
        {
            "adress": "ул.Гагарина, 1, Алтай",
            "name": "Super Hotel",
            "stars": 5
        }
    ]
    return hotels


class ShemaBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date


@app.post("/bookings")
def add_booking(booking: ShemaBooking):
    pass
