from core.security import Auth, Hasher

def test_get_password_hash():
    password = "hello"
    assert Hasher.get_password_hash(password) != password
    assert len(Hasher.get_password_hash(password)) > len(password)

def test_verify_password():
    password = "hello"
    password_hashed = Hasher.get_password_hash(password)
    assert Hasher.verify_password(password, password_hashed) == True

def test_create_access_token():
    data = {"sub": "test@test.com"}
    access_token = Auth.create_access_token(data)
    assert isinstance(access_token, str) == True