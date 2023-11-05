from pydantic import BaseModel
from typing import Optional


class FormData(BaseModel):
    # user id that is a foreign key to the user table
    user_id: int
    form_id: Optional[int] = None
    car_make: str
    car_model: str
    car_color: str
    car_license_plate_num: str
