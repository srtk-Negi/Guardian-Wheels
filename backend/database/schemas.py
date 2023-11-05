from pydantic import BaseModel
from typing import Optional


class FormData(BaseModel):
    user_id: int
    form_id: Optional[int] = None
    car_make: int
    car_model: str
    car_color: str
    car_license_plate_num: str
