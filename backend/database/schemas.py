from pydantic import BaseModel
from typing import Optional


class FormDataSchema(BaseModel):
    user_id: int
    form_id: Optional[int] = None
    car_make: int
    car_model: str
    car_color: str
    license_plate_num: str


class DeviceDataSchema(BaseModel):
    user_id: int
    device_id: Optional[int] = None
    latitude: float
    longitude: float
    path_to_image: str
