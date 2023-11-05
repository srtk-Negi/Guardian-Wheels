from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(80), unique=True)
    password = Column(String(80))


class DeviceData(Base):
    __tablename__ = 'device_data'

    device_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer)
    latitude = Column(Float)
    longitude = Column(Float)
    path_to_image = Column(String(80))
