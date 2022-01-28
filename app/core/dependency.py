from fastapi import Depends, HTTPException, status, Security
from jose import jwt
from pydantic import ValidationError
from fastapi.security import OAuth2PasswordBearer
from typing import Optional

from app import models, schemas
from app.core.config import get_app_settings

settings = get_app_settings()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_current_user(token: str = Security(oauth2_scheme)) -> Optional[models.User]:
    try:
        payload = jwt.decode(token, 
                    settings.secret_key.get_secret_value(), 
                    algorithms=settings.token_algorithm)
        user_id = payload['user_id']
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    user = await models.User.get(id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# def get_current_user(
#     token: str = Depends(oauth2_scheme)
# ) -> models.User:
#     try:
#         payload = jwt.decode(
#             token, settings.SECRET_KEY, algorithms=[security.ALGORITHM]
#         )
#         token_data = schemas.TokenPayload(**payload)
#     except (jwt.JWTError, ValidationError):
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN,
#             detail="Could not validate credentials",
#         )
#     user = crud.user.get(db, id=token_data.sub)

#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user