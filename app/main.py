from fastapi import FastAPI
from .routes import authroutes

app= FastAPI()
app.include_router(authroutes.router)

@app.get("/")
def root():
     print("Root route accessed!") 
     return {"message": "Welcome to FastAPI E-commerce!"}
handler = app