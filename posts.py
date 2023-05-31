from fastapi import status,HTTPException,Depends ,APIRouter
from typing import Optional,List
import models,schemas,utils,Oauth2
from database import  get_db
from sqlalchemy.orm import Session , joinedload 


router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)


#  GET POSTS
@router.get("/",response_model=List[schemas.Post])
def getpost(db : Session = Depends(get_db)):
    posts = db.query(models.Post).options(joinedload(models.Post.comments)).all()

    return posts


#  GET USERS POSTS

@router.get("/UsersPost",response_model=List[schemas.Post])
def latestPost(db : Session = Depends(get_db),current_user : int = Depends(Oauth2.get_current_user)):
    # sourcery skip: inline-immediately-returned-variable

    posts = db.query(models.Post).filter(models.Post.author_id == int(current_user.id)).order_by(models.Post.id.desc()).all()
    return posts


#  CREATE POST

@router.post("/createposts",status_code=status.HTTP_201_CREATED,response_model=schemas.Post)
def create_post(post:schemas.CreatePost,db : Session = Depends(get_db),current_user : int = Depends(Oauth2.get_current_user)):

    print(current_user)
    new_post = models.Post(author_id = current_user.id, **post.dict())  
    db.add(new_post)
    db.commit()
    db.refresh(new_post) 
    return new_post

#  GET POST BY ID 

@router.get("/{id}",response_model=schemas.Post)
def get_post(id: int,db : Session = Depends(get_db)):
    if post := db.query(models.Post).filter(models.Post.id == id).first():
        return post
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id : {id} Not found")
    
#  DELETE POST BY ID 


@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id : int,db : Session = Depends(get_db),current_user : int = Depends(Oauth2.get_current_user)):
    
    post_query = db.query(models.Post).filter(models.Post.id == id)

    post = post_query.first()
    print(post)
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id : {id} Not found")

    if post.user_id != int(current_user.id) :
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not Authorised to perform reqested action")

    post_query.delete(synchronize_session=False)
    db.commit()
    return {"message" : "post deleted"}



#  UPDATE POST BY ID


@router.put("/{id}")
def updatePost(id: int, updated_post: schemas.UpdatePost,db : Session = Depends(get_db),current_user : int = Depends(Oauth2.get_current_user)):
 

    post_query = db.query(models.Post).filter(models.Post.id == id)

    post = post_query.first()
    # print(post)
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id : {id} Not found")
    if post.user_id != int(current_user.id) :
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not Authorised to perform reqested action")
    post_query.update(updated_post.dict(),synchronize_session=False)

    db.commit()
    return post_query.first()
