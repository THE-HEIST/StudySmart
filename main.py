from src.data_processing_module.config import Users, Assignments
from src.core.authentication.controllers import LogIn, LogOut, SignUp
from src.core.authentication.session import load_session
from src.core.common.product import main

WELLCOME_TEXT = """
********************

WELLCOME TO STUDYSMART

********************
"""

def print_menu(items):
    header = ["No", "Function Name"]
    print("{:<5} {:<35}".format(*header))
    print("-" * 45)
    for no, name in items:
        print("{:<5} {:<35}".format(no, name))

print(WELLCOME_TEXT)

"""
check_login = load_session()
if check_login == None:
    print("No current user detected\n")
    print_menu([
        (1, "Login to use Studysmart"),
        (2, "Signup to use Studysmart")
    ])
    print("\n")
    mode = int(input("Choose your steps (1 or 2): "))
    if mode == 1:
        check = LogIn()
        while check == False:
            print("Invalid username or password. Please try again.")
            check = LogIn()
        main()
    else:
        check = SignUp()
        while check == False:
            print("Invalid input. Please try again.")
            check = SignUp()
        main()
else:
    username = check_login.get('username') if isinstance(check_login, dict) else check_login
    print(f"Hello! {username}\n You are already logged in.\n")
    print_menu([
        (1, "Continue to using Studysmart"),
        (2, "Log out")
    ])
    print("\n")
    mode = int(input("Choose your steps (1 or 2): "))
    if mode == 1:
        main()
    else:
        LogOut()
"""

main()