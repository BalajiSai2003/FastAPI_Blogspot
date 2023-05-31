from fastapi import FastAPI


models.Base.metadata.create_all(bind=engine)

app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World"}