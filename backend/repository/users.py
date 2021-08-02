from sqlalchemy.orm import Session
from schemas.users import UserSchema
from models.users import User
from core.security import Hasher

def create_new_user(user: UserSchema, db: Session):
    user = User(
        username = user.username,
        email = user.email,
        password = Hasher.get_password_hash(user.password),
        is_active = True,
        is_superuser = False
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user