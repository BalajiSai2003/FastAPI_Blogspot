from jose import JWTError,jwt
from datetime import datetime , timedelta
import schemas
from fastapi import Depends,status,HTTPException
from fastapi.security import OAuth2PasswordBearer 


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
#secret key
#algorithm
#Expiration time

SECRET_KEY = "HELLO"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data : dict):
    # sourcery skip: aware-datetime-for-utc, inline-immediately-returned-variable
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode["exp"] = expire
    encoded_jwt = jwt.encode(to_encode ,SECRET_KEY ,algorithm=ALGORITHM)

    return encoded_jwt

def verify_access_token(token : str, credentisl_exception):
    # sourcery skip: raise-from-previous-error

    try:

        payload = jwt.decode(token, SECRET_KEY,algorithms=[ALGORITHM])

        id : str  = payload.get("user_id")
        type : str = payload.get("user_type")
    

        if id is None or type is None:
            raise credentisl_exception
        token_data = schemas.Token_data(id=id, type=type)
            
    
    except JWTError:
        raise credentisl_exception
    
    return token_data
    


    
def get_current_user(token : str = Depends(oauth2_scheme)):
    credentisl_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Could not validate credentials" , headers={"WWW-Authenticate":"Bearer"})
    return verify_access_token(token,credentisl_exception)