from src.data_processing_module.config import Users
import hashlib
from .session import load_session, save_session, clear_session


def SignUp():
    username = input("What is your name: ")
    password = input("Password: ")

    password = hashlib.sha256(password.encode()).digest()

    Users.add("users", {"username":username,"password":password})

    if load_session() == None:
        save_session(username)
        return True
    else:
        return False

def LogIn():
    username = input("What is your name: ")
    password = input("Password: ")

    user = Users.find("users", {"username":username})
    password = hashlib.sha256(password.encode()).digest()
    if user and user["password"]:
        if load_session() == None:
            save_session(username)
            return True
        else:
            return False

def LogOut():
    if load_session != None:
        clear_session()
        return True
    else: 
        return False
