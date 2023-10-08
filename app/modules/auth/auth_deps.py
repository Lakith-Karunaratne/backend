# import secrets
# from typing import Generator
# from app.db.database import SessionLocal
# from app.modules.auth import auth_schema
# from app.env import APPENV
# from jose import jwt
# from fastapi.exceptions import HTTPException
# from fastapi import status, Depends
# from pydantic import ValidationError
# from sqlalchemy.orm import Session
# from app.models import model as models
# from fastapi.security import OAuth2PasswordBearer


# # secret_key_dict = APPENV.get_skey()
# # secret_key = secret_key_dict['key']
# SECRET_KEY: str = secrets.token_urlsafe(32)

# JWT_ALGO: str = "HS512"

# # ACCESS_TOKEN_EXPIRE_SECONDS: int = 60 * 30
# # REFRESH_TOKEN_EXPIRE_SECONDS: int = 60 * 60 * 24 * 30

# reusable_oauth2 = OAuth2PasswordBearer(tokenUrl=f"/login/oauth")


# def get_db() -> Generator:
#     try:
#         db = SessionLocal()
#         yield db
#     finally:
#         db.close()


# def get_token_payload(token: str) -> auth_schema.TokenPayload:
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[JWT_ALGO])
#         token_data = auth_schema.TokenPayload(**payload)
#     except (jwt.JWTError, ValidationError):
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN,
#             detail="Could not validate credentials",
#         )
#     return token_data

# def get_current_user(db: Session = Depends(get_db), token: str = Depends(reusable_oauth2)) -> models.User:
#     token_data = get_token_payload(token)
#     if token_data.refresh or token_data.totp:
#         # Refresh token is not a valid access token and TOTP True can only be used to validate TOTP
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN,
#             detail="Could not validate credentials",
#         )
#     user = models.User.get_user(username=token_data.sub)
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user

# def get_refresh_user(db: Session = Depends(get_db), token: str = Depends(reusable_oauth2)) -> models.User:
#     token_data = get_token_payload(token)
#     if not token_data.refresh:
#         # Access token is not a valid refresh token
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN,
#             detail="Could not validate credentials",
#         )
#     user = models.User.get_user(username=token_data.sub)
#     # user = crud.user.get(db, id=token_data.sub)
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     # if not crud.user.is_active(user):
#     #     raise HTTPException(status_code=400, detail="Inactive user")
#     # Check and revoke this refresh token
#     token_obj = crud.token.get(token=token, user=user)
#     if not token_obj:
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN,
#             detail="Could not validate credentials",
#         )
#     crud.token.remove(db, db_obj=token_obj)
#     return user


# def get_current_active_user(
#     current_user: models.User = Depends(get_current_user),
# ) -> models.User:
#     if not crud.user.is_active(current_user):
#         raise HTTPException(status_code=400, detail="Inactive user")
#     return current_user


# def get_current_active_superuser(
#     current_user: models.User = Depends(get_current_user),
# ) -> models.User:
#     if not crud.user.is_superuser(current_user):
#         raise HTTPException(status_code=400, detail="The user doesn't have enough privileges")
#     return current_user