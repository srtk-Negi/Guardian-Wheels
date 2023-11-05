from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/formdata")
def formdata(payload: dict = Body(...)):
    print(payload)
    return payload
