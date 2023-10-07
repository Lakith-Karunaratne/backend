# from passlib.context import CryptContext
# from passlib.exc import UnknownHashError
import secrets
from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
# from app.env import APPENV
from fastapi.responses import RedirectResponse
# verification_code_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
from fastapi_login import LoginManager
from fastapi_login.exceptions import InvalidCredentialsException
from app.db.database import SessionManager
from app.models.model import User, password_context
from passlib.exc import UnknownHashError
from datetime import timedelta

# _secret = APPENV.get_skey()
_secret: str = secrets.token_urlsafe(32)

print(_secret)
router = APIRouter(tags=["Auth"])

# oauth2scheme = OAuth2PasswordBearer(tokenUrl='token')

login_manager = LoginManager(secret=_secret, token_url='/token',use_cookie=True) # Expose to secure the endpoints
login_manager.cookie_name = 'pbl_app_be'

def verify_password(plain_password, hashed_password):
    try:
        result = password_context.verify(plain_password, hashed_password)
        return result
    except UnknownHashError:
        return False


@login_manager.user_loader()
def query_user(username: str):  # , db: Session = Depends(get_db)):
    with SessionManager() as database:
        result = database.query(User).filter(User.username == username).first()
    return result

@router.post('/token')
def login(data:OAuth2PasswordRequestForm = Depends()):
    username = data.username
    password = data.password
    
    user = query_user(username) #Find User

    with SessionManager() as db:
        if not user:
            raise InvalidCredentialsException
        
        elif not verify_password(password, user.pw_hash):
            raise InvalidCredentialsException
    
    token = login_manager.create_access_token(
        expires=timedelta(minutes=60),
        data={'sub': username,
              'username': user.username,
              'email': user.email}
    )

    return {
        "access_token":token,
        "token_type": 'bearer'
    }


@router.get("/test/")
async def read_items(token: str = Depends(login_manager)):
    return {"token": token}


