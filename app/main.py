from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI with PostgreSQL and pgAdmin is running successfully!"}
