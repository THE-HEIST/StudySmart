#from src.authentication.controllers import LogOut, LogIn, SignUp
from src.core.authentication.session import load_session, save_session, clear_session
from src.data_processing_module.config4test import test_users_db as Users
import pytest

def test_save_session():
    # Clear the session before testing
    clear_session(test="test/session.txt")
    
    # Save a session for a test user
    save_session("testuser", test="test/session.txt")
    
    # Load the session and check if it matches the saved username
    loaded_username = load_session(test="test/session.txt")
    assert loaded_username is not None and loaded_username.get("username") == "testuser"

def test_clear_session():
    # Save a session for a test user
    save_session("testuser", test="test/session.txt")
    
    # Clear the session
    clear_session(test="test/session.txt")
    
    # Load the session and check if it is cleared (should return None)
    loaded_username = load_session(test="test/session.txt")
    assert loaded_username is None

def test_load_session_no_session():
    # Clear the session before testing
    clear_session(test="test/session.txt")
    
    # Load the session when no session is saved (should return None)
    loaded_username = load_session(test="test/session.txt")
    assert loaded_username is None

def test_load_session_with_session():
    # Save a session for a test user
    save_session("testuser", test="test/session.txt")
    
    # Load the session and check if it matches the saved username
    loaded_username = load_session(test="test/session.txt")
    assert loaded_username is not None and loaded_username.get("username") == "testuser"
    