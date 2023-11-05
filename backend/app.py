from fastapi import FastAPI, status, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import FormDataSchema, FormData, DeviceData, DeviceDataSchema, get_db
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["http://localhost",
           "http://localhost:8000", "http://127.0.0.1:5500"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/forms/create", response_model=FormDataSchema, status_code=status.HTTP_201_CREATED)
def create_form(form: FormDataSchema, db: Session = Depends(get_db)):
    new_form = FormData(**form.model_dump())
    db.add(new_form)
    db.commit()
    db.refresh(new_form)
    return new_form


@app.get("/forms/{user_id}", response_model=FormDataSchema)
def read_item(user_id: int, db: Session = Depends(get_db)):
    item = db.query(FormData).filter(FormData.user_id == user_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.post("/deviceData/create", response_model=DeviceDataSchema, status_code=status.HTTP_201_CREATED)
def create_form(form: DeviceDataSchema, db: Session = Depends(get_db)):
    new_form = DeviceData(**form.model_dump())
    db.add(new_form)
    db.commit()
    db.refresh(new_form)
    return new_form


@app.get("/deviceData/{user_id}", response_model=DeviceDataSchema)
def read_item(user_id: int, db: Session = Depends(get_db)):
    item = db.query(DeviceData).filter(DeviceData.user_id == user_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
