from pathlib import Path
from ..LangaDB.controllers import LangaDB

DATA_DIRECTORY = Path(__file__).resolve().parent.parent / "data"

Users = LangaDB(str(DATA_DIRECTORY/"users.json"),{"users": []})
Assignments = LangaDB(str(DATA_DIRECTORY/"assignments.json",{"assignments":[]}))