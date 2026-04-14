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

    def add_guest(self, name, email, type_=Guest.REGULAR):
        guest = Guest(name, email, type_)
        self.guest.append(guest)
        return guest
    def delete_guest(self,guest_index = int):
        if self.id








# TODO: Implement Room class here


# TODO: Implement Hotel class here
