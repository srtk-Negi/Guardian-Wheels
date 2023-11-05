from sqlalchemy import Column, Integer, String, Float
from .db import base


class FormData(base):
    __tablename__ = 'forms'

    form_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer)
    car_make = Column(Integer)
    car_model = Column(String(50))
    car_color = Column(String(50))
    license_plate_num = Column(String(12))


class DeviceData(base):
    __tablename__ = 'device_data'

    device_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer)
    latitude = Column(Float)
    longitude = Column(Float)
    path_to_image = Column(String(80))
