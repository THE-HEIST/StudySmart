from pathlib import Path
from src.data_processing_module.config import Users

SESSION_FILE = Path(__file__).resolve().parent.parent / "data" / "session.txt"

def save_session(username: str, test=None):
    if test is not None:
        SESSION_FILE = Path(test) / "session.txt"
    SESSION_FILE.write_text(username, encoding="utf-8")

def load_session(test=None):
    if test is not None:
        SESSION_FILE = Path(test) / "session.txt"
    if not SESSION_FILE.exists():
        return None
    username = SESSION_FILE.read_text(encoding="utf-8").strip()
    if not username:
        return None
    return Users.find("users", "username", username)

def clear_session(test=None):
    if test is not None:
        SESSION_FILE = Path(test) / "session.txt"
    if SESSION_FILE.exists():
        SESSION_FILE.write_text("", encoding="utf-8")