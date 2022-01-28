from datetime import datetime, timedelta
from pydantic import UUID4
import uuid
from typing import List, Optional, Tuple
from jose import jwt
from passlib.context import CryptContext

from app.schemas import *
from app.core.config import get_app_settings


settings = get_app_settings()
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_and_update_password(
    plain_password: str, hashed_password: str
) -> Tuple[bool, str]:
    return password_context.verify_and_update(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return password_context.hash(password)


async def authenticate(credentials: LoginSchema) -> Optional[User]:
    if credentials.email:
        user = await User.get_by_email(credentials.email)
    else:
        return None

    if user is None:
        return None

    verified, updated_password_hash = verify_and_update_password(
        credentials.password.get_secret_value(), user.hashed_password
    )

    if not verified:
        return None
        # Update password hash to a more robust one if needed
    if updated_password_hash is not None:
        user.password_hash = updated_password_hash
        await user.save()
    return user

def get_token(data: dict, expires_delta: int):
    pass
    to_encode = data.copy()
    to_encode.update({
        "exp": datetime.utcnow() + timedelta(seconds=expires_delta),
        "iss": settings.title
    })
    return jwt.encode(
        to_encode,
        settings.secret_key.get_secret_value(),
        algorithm=settings.token_algorithm
    )


def get_access_token(user_id: UUID4):
    jti = uuid.uuid4()
    claims = {
        "user_id": str(user_id),
    }
    return {
        "jti": jti,
        "token": get_token(
            claims,
            settings.token_lifetime
        )
    }
