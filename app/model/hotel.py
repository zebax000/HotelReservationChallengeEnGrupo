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
    type_: str = field(default = REGULAR)

    def __str__(self) -> str:
        return f"Guest{self.name}, ({self.email}) of type {self.type_}"

# TODO: Implement Reservation class here
class Reservation:
    guest_name: str
    description: str
    check_in: date
    check_out: date
    guest: list[Guest] = field(init =  False, default_factory = list)
    id: str = field(default_factory = generate_unique_id())
    services: list["HotelService"] = field(default_factory=list)

    def add_guest(self, name, email, type_=Guest.REGULAR):
        guest = Guest(name, email, type_)
        self.guest.append(guest)
        return guest

    def delete_guest(self,guest_index = int):
        if 0 <= guest_index < len(self.guest):
            self.guest.pop(guest_index)
        else:
            guest_not_found_error()

    def __len__(self):
        return (self.check_out - self.check_in).days


class Room:

    def __init__(self, number: int, type_: str, price_per_night: float):
        self.number: int = number
        self.type_: str = type_
        self.price_per_night: float = price_per_night
        self.availability: dict[date, str | None] = {}

        self._init_availability()

    def _init_availability(self) -> None:
        today = datetime.now().date()
        for i in range(365):
            current_date = today + timedelta(days=i)
            self.availability[current_date] = None

    def book(self, reservation_id: str, check_in: date, check_out: date) -> None:
        current_date = check_in
        dates_to_book = []

        while current_date < check_out:
            if self.availability.get(current_date) is not None:
                room_not_available_error()
                return
            dates_to_book.append(current_date)
            current_date += timedelta(days=1)

        for booked_date in dates_to_book:
            self.availability[booked_date] = reservation_id

    def release(self, reservation_id: str):
        released = False
        for d, saved_id in self.availability.items():
            if saved_id == reservation_id:
                self.availability[d] = None
                released = True
        if not released:
            reservation_not_found_error()

    def update_booking(self, reservation_id: str, check_in: date, check_out: date):
        for d in self.availability:
            if self.availability[d] == reservation_id:
                self.availability[d] = None

        current = check_in
        while current < check_out:
            if self.availability.get(current) is not None:
                room_not_available_error()
            else:
                self.availability[current] = reservation_id
            current += timedelta(days=1)


# TODO: Implement Hotel class here

class Hotel:
    def __init__(self):
        rooms: dict[int, Room] = {}
        reservations: dict[str, Reservation] = {}

    def add_room(self, number: int, type_: str, price_per_night: float):
        if number in self.rooms:
            room_already_exists_error()
        else:
            room = Room(number, type_, price_per_night)
            self.rooms[number] = room
    def make_reservation(self, gest_name: str, description: str, room_number: int, check_in: date, check_out: date ):
        ...




@dataclass
class HotelService:
    name: str
    price: float
    description: str = ""
    date_used: date | None = None

    def __str__(self) -> str:
        date_info = f" | Date: {self.date_used}" if self.date_used else ""
        return f"Service: {self.name} | Price: ${self.price}{date_info} | Description: {self.description}"























