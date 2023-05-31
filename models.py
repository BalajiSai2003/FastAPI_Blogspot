from database import Base
from sqlalchemy import Column ,Integer ,String, Boolean, ForeignKey, Enum
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    id  = Column(Integer,primary_key = True,nullable = False)
    name = Column(String, nullable = True)
    email = Column(String, nullable = False ,unique = True)
    password = Column(String, nullable = False)
    created_at  = Column(TIMESTAMP,nullable = False ,server_default = text('now()'))  
    posts = relationship("Post", back_populates="author")
    comments = relationship("Comment", back_populates="author") 



class Post(Base):
    __tablename__  = "posts"
    id  = Column(Integer,primary_key = True,nullable = False)
    title = Column(String,nullable = False)
    content  = Column(String,nullable = False)
    published  = Column(Boolean ,server_default  = "True")
    created_at  = Column(TIMESTAMP,nullable = False ,server_default = text('now()'))

    author_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable = False)

    author = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="post")


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    created_at  = Column(TIMESTAMP,nullable = False ,server_default = text('now()'))
    author_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable = False)
    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), nullable = False)

    author = relationship("User", back_populates="comments")
    post = relationship("Post", back_populates="comments")