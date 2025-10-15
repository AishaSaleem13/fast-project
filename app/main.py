from fastapi import FastAPI
from app.routes import authroutes
from mangum import Mangum

app = FastAPI()

app.include_router(authroutes.router)

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI E-commerce!"}

handler = Mangum(app)
