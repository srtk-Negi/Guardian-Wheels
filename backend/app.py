from fastapi import FastAPI, status
from fastapi.params import Body
from .database import get_engine, FormData
from sqlalchemy import insert

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/form")
def form_data(data: FormData = Body(...)):
    try:
        engine = get_engine()
        insert_query = insert(FormData).values(
            user_id=data.user_id,
            form_id=data.form_id,
            car_make=data.car_make,
            car_model=data.car_model,
            car_color=data.car_color,
            car_license_plate_num=data.car_license_plate_num
        )
        with engine.begin() as conn:
            conn.execute(insert_query)
        return {"message": "success"}
    except Exception as e:
        raise status.HTTP_500_INTERNAL_SERVER_ERROR
