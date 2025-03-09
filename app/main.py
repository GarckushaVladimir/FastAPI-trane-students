from fastapi import FastAPI
from app.students.router import router as router_students

app = FastAPI()


@app.get("/")
def home_page():
    return {"message": "Hello!"}


app.include_router(router_students)
