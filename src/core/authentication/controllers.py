from src.data_processing_module.config import Users
import hashlib
from .session import load_session, save_session, clear_session


def SignUp(Users=Users, test=None):
    username = input("What is your name: ")
    password = input("Password: ")

    password = str(hashlib.sha256(password.encode()).hexdigest())

    user = Users.find("users", "username", username)
    if user:
        return False  # User already exists

    Users.add("users", {"username":username,"password":password})

    if load_session(test=test) == None:
        save_session(username, test=test)
        return True
    else:
        return False

def LogIn(Users=Users, test=None):
    username = input("What is your name: ")
    password = input("Password: ")

    user = Users.find("users", "username", username)
    password = str(hashlib.sha256(password.encode()).hexdigest())
    if user and user["password"] and password == user["password"]:
        if load_session(test=test) == None:
            save_session(username, test=test)
            return True
        else:
            return False

def LogOut(Users=Users, test=None):
    clear_session(test=test)
    return True
