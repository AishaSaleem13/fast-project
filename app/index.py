from fastapi import FastAPI
from app.routes import authroutes

app = FastAPI()

app.include_router(authroutes.router)

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI E-commerce!"}


