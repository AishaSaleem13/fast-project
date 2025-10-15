from fastapi import FastAPI
from .routes import authroutes
from mangum import Mangum 

app= FastAPI()
app.include_router(authroutes.router)

@app.get("/")
def root():
     print("Root route accessed!") 
     return {"message": "Welcome to FastAPI E-commerce!"}
handler = Mangum(app)