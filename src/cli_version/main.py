from src.data_processing_module.config import Users, Assignments
from src.core.authentication.controllers import LogIn, LogOut, SignUp
from src.core.authentication.session import load_session

WELLCOME_TEXT = """
********************

WELLCOME TO STUDYSMART

********************
"""

print(WELLCOME_TEXT)

check_login = load_session()
if check_login == None:
    print("No current user detected")
    print("""
   ********************
   1. Login to use Studysmart
   2. Signup to use Studysmart 
""")
    mode = int(input("Choose your steps (1 or 2): "))
    if mode == 1:
        LogIn()
    else:
        SignUp()
else:
    print(f"Hello! {check_login}")
    print("""
       ********************
       1. Continue to using Studysmart
       2. Log out
    """)
    mode = int(input("Choose your steps (1 or 2): "))
    if mode == 1:
        LogIn()
    else:
        LogOut()