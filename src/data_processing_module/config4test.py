from LangaDB import LangaDB
from pathlib import Path

dir_path = Path(__file__).resolve().parent.parent.parent

test_assignments = dir_path / "data" / "test" / "assignments.json"
test_users = dir_path / "data" / "test" / "users.json"

test_assignments_db = LangaDB(test_assignments)
test_users_db = LangaDB(test_users)