from pathlib import Path
<<<<<<< HEAD
from ..LangaDB.controllers import LangaDB

DATA_DIRECTORY = Path(__file__).resolve().parent.parent / "data"

Users = LangaDB(str(DATA_DIRECTORY/"users.json"),{"users": []})
Assignments = LangaDB(str(DATA_DIRECTORY/"assignments.json",{"assignments":[]}))
=======
from src.LangaDB.controllers import LangaDB

DATA_DIRECTORY = Path(__file__).resolve().parent.parent / "data"

Users = LangaDB(db_path=str(DATA_DIRECTORY/"users.json"),default_data={"users": []})
Assignments = LangaDB(db_path=str(DATA_DIRECTORY/"assignments.json"),default_data={"assignments":[]})
>>>>>>> EasiestCode
