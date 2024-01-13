from fastapi import FastAPI, Query
from typing import Optional
from datetime import date
from pydantic import BaseModel


app = FastAPI()


class ShemaHotel(BaseModel):
    adress: str
    name: str
    stars: int



@app.get("/hotels/", response_model=list[ShemaHotel])
def get_hotels(
    location: str,
    date_from: date,
    date_to: date,
    stars: Optional[int] = Query(None, ge=1, le=5),
    has_spa: Optional[bool] = None
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
