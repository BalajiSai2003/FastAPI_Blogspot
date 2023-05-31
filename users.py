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

#  GET  USERS

@router.get("/",response_model=List[schemas.UserResponce])
def getUser(db : Session = Depends(get_db)):
    
    Users = db.query(models.User).order_by(models.User.id).all()

    return Users

#  GET  USERS BY EMAIL

@router.get("/{email}",response_model=schemas.UserResponce)
def get_user(email : str,db : Session = Depends(get_db)):
    # sourcery skip: reintroduce-else, swap-if-else-branches, use-named-expression
    user = db.query(models.User).filter(models.User.email == email).first()


    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with {email} not found")
    return user

#  DELETE USER BY ID


@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id : int,db : Session = Depends(get_db),user_id : int = Depends(Oauth2.get_current_user)):
    # sourcery skip: none-compare, remove-unnecessary-else

    user = db.query(models.User).filter(models.User.id == id)
    if user.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with id : {id} Not found")
    else:
        user.delete(synchronize_session=False)
        db.commit()
        return {"message" : "user deleted"}
    

#  UPDATE USER PASSWORD 



@router.put("/Update/UserPassword",response_model=schemas.UserResponce)
def updateUserName( updated_User: schemas.UpdateUserPassword,db : Session = Depends(get_db),current_user : int = Depends(Oauth2.get_current_user)):

    print(current_user.id)
    
    hashed_passsword =utils.hashPassword(updated_User.password) #hashing the user password
    updated_User.password = hashed_passsword  #ressigning it to usres password
    User_query = db.query(models.User).filter(models.User.id == int(current_user.id))



    User_query.update(updated_User.dict(),synchronize_session=False)

    db.commit()
    return User_query.first()



#  UPDATE USER NAME 


@router.put("/Update/UserName",response_model=schemas.UserResponce)
def updateUserName( updated_User: schemas.UpadteUserName,db : Session = Depends(get_db),current_user : int = Depends(Oauth2.get_current_user)):

    print(current_user.id)
    

    User_query = db.query(models.User).filter(models.User.id == int(current_user.id))



    User_query.update(updated_User.dict(),synchronize_session=False)

    db.commit()
    return User_query.first()


#  UPDATE USER EMAIL 

@router.put("/Update/UserEmail",response_model=schemas.UserResponce)
def updateUserEmail( updated_User: schemas.UpadteUserEmail,db : Session = Depends(get_db),current_user : int = Depends(Oauth2.get_current_user)):
    

    User_query = db.query(models.User).filter(models.User.id == int(current_user.id))


    User_query.update(updated_User.dict(),synchronize_session=False)

    db.commit()
    return User_query.first()
