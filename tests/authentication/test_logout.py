from src.core.authentication.controllers import LogOut, LogIn, SignUp
import pytest
from src.data_processing_module.config4test import test_users_db as Users

def test_logout(monkeypatch):
    # Clear the session before testing
    Users.clear_all("users")
    
    # Simulate a logged-in user by saving a session
    Users.add("users", {"username": "testuser", "password": "testpassword"})

    inputs = iter([
        "testuser",  # Username
        "testpassword"  # Password
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    LogIn(Users=Users, test="test/session.txt")
    
    # Call the LogOut function
    result = LogOut(Users=Users, test="test/session.txt")
    
    # Check if the function returns True indicating successful logout
    assert result == True
    
    # Check if the session is cleared (no current user)
    assert Users.find("users", "username", "testuser") is not None  # User still exists in the database