from fastapi import FastAPI
import models
import users,auth
from database import engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World"}




app.include_router(users.router)

app.include_router(auth.router)