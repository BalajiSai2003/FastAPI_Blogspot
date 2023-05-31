import sys
sys.path.append("..")

from fastapi import status,HTTPException,Depends,APIRouter
from typing import List
import models,schemas,utils,Oauth2
from database import  get_db
from sqlalchemy.orm import Session  

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

# CREATING USERS

@router.post("/createUser",status_code=status.HTTP_201_CREATED ,response_model=schemas.UserResponce)
def createUser(user :schemas.UserCreate ,db : Session = Depends(get_db)):

    ########## SALTING ############
    hashed_passsword =utils.hashPassword(user.password) #hashing the user password
    user.password = hashed_passsword  #ressigning it to usres password
    newUser = models.User(**user.dict())
    db.add(newUser)
    db.commit()
    db.refresh(newUser)

    return newUser

