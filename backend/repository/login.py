from sqlalchemy.orm import Session
from jose import jwt
from typing import Optional
from datetime import datetime, timedelta
from core.config import settings
from models.users import User
from core.security import Hasher


def get_user(username: str, db: Session)-> User:
    user = db.query(User).filter(User.email == username).first()
    return user

def authenticate_user(username: str, password: str, db: Session):
    user = get_user(username, db)
    if not user:
        return False
    if not Hasher.verify_password(password, user.password):
        return False
    
    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes = settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm = settings.JWT_ALGORITHM)
    return encoded_jwt