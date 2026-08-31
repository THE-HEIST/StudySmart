from src.core.authentication.controllers import LogIn, LogOut, SignUp
from src.core.authentication.session import load_session, clear_session
from src.data_processing_module.config4test import test_users_db as Users

def test_signup(monkeypatch):
    Users.clear_all("users")
    clear_session(test="test/session.txt")

    inputs = iter([
        "testuser",  # Username
        "testpassword"  # Password
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    x = SignUp(Users=Users, test="test/session.txt")

    assert x == True
    assert Users.find("users", "username", "testuser") is not None  # User exists in the database

def test_signup_existing_user(monkeypatch):
    Users.clear_all("users")
    clear_session(test="test/session.txt")
    
    Users.add("users", {"username": "testuser", "password": "testpassword"})
    inputs = iter([
        "testuser",  # Username
        "testpassword"  # Password
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    x = SignUp(Users=Users, test="test/session.txt")

    assert x == False  # Should return False since the user already exists

