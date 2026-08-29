import pytest
from src.core.authentication.controller import LogIn
from src.data_processing_module.config4test import test_user_db as Users
import hashlib

def test_login(monkeypatch):
    Users.clear_all("users")
    Users.add("users", {"username": "testuser", "password": hashlib.sha256("testpassword".encode()).digest()})

    inputs = iter([
        "testuser",  # Username
        "testpassword"  # Password
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    x = LogIn(Users=Users, test="tests/authentication/test_session.txt")

    assert x == True
    assert Users.find("users", "username", "testuser") is not None  # User still exists in the database

def test_login_dont_exist(monkeypatch):
    Users.clear_all("users")
    inputs = iter([
        "testuser",  # Username
        "testpassword"  # Password
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    x = LogIn(Users=Users, test="tests/authentication/test_session.txt")

    assert x == None
    assert Users.find("users", "username", "testuser") is None  # User does not exist in the database

def test_login_wrong_password(monkeypatch):
    Users.clear_all("users")
    Users.add("users", {"username": "testuser", "password": hashlib.sha256("testpassword".encode()).digest()})
    inputs = iter([
        "testuser",  # Username
        "wrongpassword"  # Wrong Password
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    x = LogIn(Users=Users, test="tests/authentication/test_session.txt")
    assert x == None
    assert Users.find("users", "username", "testuser") is not None  # User still exists in the database