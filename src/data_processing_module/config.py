from pathlib import Path
<<<<<<< HEAD
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
=======
from src.LangaDB.controllers import LangaDB

DATA_DIRECTORY = Path(__file__).resolve().parent.parent / "data"

Users = LangaDB(db_path=str(DATA_DIRECTORY/"users.json"),default_data={"users": []})
Assignments = LangaDB(db_path=str(DATA_DIRECTORY/"assignments.json"),default_data={"assignments":[]})
>>>>>>> a524f49cccca3ba2298e5f8411e810d123d52f66
