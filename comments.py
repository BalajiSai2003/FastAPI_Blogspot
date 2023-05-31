from fastapi import status,HTTPException,Depends ,APIRouter
from typing import Optional,List
import models,schemas,utils,Oauth2
from database import  get_db
from sqlalchemy.orm import Session , joinedload 


router = APIRouter(
    prefix="/posts",
    tags=["COMMENTS"]
)





#  CREATE COMMENT

@router.post("/{post_id}/comments",status_code=status.HTTP_201_CREATED)
def create_comment(post_id : int ,comment:schemas.CommentCreate,db : Session = Depends(get_db),current_user : int = Depends(Oauth2.get_current_user)):
    new_comment = models.Comment(author_id = current_user.id,post_id = post_id ,**comment.dict())  
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment) 
    return new_comment




#  GET COMMENTS BY POST ID 

@router.get("/{post_id}/comments")
def get_comments(post_id: int,db : Session = Depends(get_db)):
    if comments := db.query(models.Comment).filter(models.Comment.post_id == post_id).all():
        return comments
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id : {id} Not found")




#  DELETE COMMENT BY ID 


@router.delete("/CommentDelete/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_comment(id : int,db : Session = Depends(get_db),current_user : int = Depends(Oauth2.get_current_user)):
    
    query = db.query(models.Comment).filter(models.Comment.id == id)

    comment = query.first()
    print(comment)
    if comment is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"comment with id : {id} Not found")

    if comment.author_id != int(current_user.id) :
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not Authorised to perform reqested action")

    query.delete(synchronize_session=False)
    db.commit()
    return {"message" : "comment deleted"}



#  UPDATE POST BY ID


@router.put("/UpdateComment/{id}")
def update_comment(id: int, update_comment: schemas.CommentUpdate,db : Session = Depends(get_db),current_user : int = Depends(Oauth2.get_current_user)):
 

    query = db.query(models.Comment).filter(models.Comment.id == id)

    comment = query.first()
    # print(comment)
    if comment is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"comment with id : {id} Not found")
    if comment.author_id != int(current_user.id) :
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not Authorised to perform reqested action")
    query.update(update_comment.dict(),synchronize_session=False)

    db.commit()
    return query.first()
