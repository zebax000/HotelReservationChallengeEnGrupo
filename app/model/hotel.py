from dataclasses import dataclass, field
from datetime import datetime, date, timedelta
from typing import ClassVar

from app.services.util import (generate_unique_id, date_lower_than_today_error,
    reservation_not_found_error, guest_not_found_error, room_not_available_error,
    room_not_found_error, room_already_exists_error)


# TODO: Implement Guest class here
@dataclass
class Guest:
    REGULAR: str = 'Regular'
    VIP: str = 'Vip'
    name: str = 'Name'
    email: str = 'Email'


# TODO: Implement Reservation class here


# TODO: Implement Room class here


# TODO: Implement Hotel class here

class Hotel:
    def __init__(self):
        rooms: dict[int, Room] = {}
        reservations: dict[str, Reservation] = {}

    def __add_room__(self, number: int, type_: str, price_per_night: float):

