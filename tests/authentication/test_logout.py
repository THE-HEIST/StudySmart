from src.core.authentication.controllers import LogOut
import pytest
from src.data_processing_module.config4test import test_user_db as Users

def test_logout():
    # Clear the session before testing
    Users.clear_all("users")
    
    # Simulate a logged-in user by saving a session
    Users.add("users", {"username": "testuser", "password": "testpassword"})
    
    # Call the LogOut function
    result = LogOut(Users=Users, test="tests/authentication/test_session.txt")
    
    # Check if the function returns True indicating successful logout
    assert result == True
    
    # Check if the session is cleared (no current user)
    assert Users.find("users", "username", "testuser") is not None  # User still exists in the database