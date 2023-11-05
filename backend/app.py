from fastapi import FastAPI, status, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import FormDataSchema, get_db, FormData


app = FastAPI()


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
