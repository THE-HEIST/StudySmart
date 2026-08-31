from pathlib import Path
from src.data_processing_module.config import Users
<<<<<<< HEAD
<<<<<<< HEAD
=======
from src.data_processing_module.config4test import test_users_db as TestUsers
>>>>>>> a524f49cccca3ba2298e5f8411e810d123d52f66

#SESSION_FILE = Path(__file__).resolve().parent.parent / "data" / "session.txt"
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent   

def save_session(username: str, test=None):
    SESSION_FILE = BASE_DIR / 'src' / "data" / "session.txt"
    if test is not None:
        SESSION_FILE = SESSION_FILE = BASE_DIR / 'src' / "data" / test
    SESSION_FILE.write_text(username, encoding="utf-8")

<<<<<<< HEAD
def load_session():
=======
from src.data_processing_module.config4test import test_users_db as TestUsers

#SESSION_FILE = Path(__file__).resolve().parent.parent / "data" / "session.txt"
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent   

def save_session(username: str, test=None):
    SESSION_FILE = BASE_DIR / 'src' / "data" / "session.txt"
    if test is not None:
        SESSION_FILE = SESSION_FILE = BASE_DIR / 'src' / "data" / test
    SESSION_FILE.write_text(username, encoding="utf-8")

=======
>>>>>>> a524f49cccca3ba2298e5f8411e810d123d52f66
def load_session(Users=Users, test=None):
    SESSION_FILE = BASE_DIR / 'src' / "data" / "session.txt"
    if test is not None:
        SESSION_FILE = SESSION_FILE = BASE_DIR / 'src' / "data" / test
        Users = TestUsers
<<<<<<< HEAD
>>>>>>> EasiestCode
=======
>>>>>>> a524f49cccca3ba2298e5f8411e810d123d52f66
    if not SESSION_FILE.exists():
        return None
    username = SESSION_FILE.read_text(encoding="utf-8").strip()
    if not username:
        return None
    return Users.find("users", "username", username)

<<<<<<< HEAD
<<<<<<< HEAD
def clear_session():
=======
=======
>>>>>>> a524f49cccca3ba2298e5f8411e810d123d52f66
def clear_session(Users=Users, test=None):
    SESSION_FILE = BASE_DIR / 'src' / "data" / "session.txt"
    if test is not None:
        SESSION_FILE = BASE_DIR / 'src' / "data" / test
<<<<<<< HEAD
>>>>>>> EasiestCode
=======
>>>>>>> a524f49cccca3ba2298e5f8411e810d123d52f66
    if SESSION_FILE.exists():
        SESSION_FILE.write_text("", encoding="utf-8")