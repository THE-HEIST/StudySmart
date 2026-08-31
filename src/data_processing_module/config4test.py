from src.LangaDB.controllers import LangaDB
from pathlib import Path

dir_path = Path(__file__).resolve().parent.parent.parent

test_assignments = dir_path / 'src' / "data" / "test" / "assignments.json"
test_users = dir_path / 'src' / "data" / "test" / "users.json"

test_assignments_db = LangaDB(db_path=str(test_assignments), default_data={"assignments": []})
test_users_db = LangaDB(db_path=str(test_users), default_data={"users": []})