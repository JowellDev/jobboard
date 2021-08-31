import random
import string
from sqlalchemy.orm import Session

from schemas.users import UserSchema
from repository.users import create_new_user

def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=32))

def create_random_owner(db: Session):
    username = random_lower_string()
    email = f"{random_lower_string()}@{random_lower_string()}.com"
    password = random_lower_string()
    user_schema = UserSchema(
        username = username,
        email = email,
        password = password
    )

    new_owner = create_new_user(user_schema, db)

    return new_owner
