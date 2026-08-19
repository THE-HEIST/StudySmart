# LangaDB usage guide

LangaDB is The-Black-Opal's mini database class. It stores data in JSON files, loads them when the app starts, and writes back on every add/update. No external packages — only Python's built-in `json` and `os`.

The project uses 2 data files in `src/data/`:

- `users.json` — user accounts
- `assignments.json` — assignment list

## Quick start

Don't create your own `LangaDB(...)` instances. Two are already set up in `config.py` — just import them:

```python
from src.data_processing_module.config import users_db, assign_db
```

Run the app from the project root, as a module:

```bash
python -m src.cli_version.main
```

Running `python src/cli_version/main.py` instead will fail with `ModuleNotFoundError: No module named 'src'`.

## What the file looks like

`assignments.json`:

```json
{
    "last_id": 2,
    "assignments": [
        {
            "id": 1,
            "name": "AI report",
            "module": "CS101",
            "owner": "lan",
            "days_left": 2,
            "difficulty": 4,
            "importance": 5,
            "completed": false,
            "score": 30
        },
        {
            "id": 2,
            "name": "Marketing essay",
            "module": "MK202",
            "owner": "lan",
            "days_left": 7,
            "difficulty": 2,
            "importance": 3,
            "completed": false,
            "score": 14
        }
    ]
}
```

`last_id` is the counter the DB uses to generate ids — don't edit it by hand. Each item is an ordinary Python dict.

## Main functions

### add — create

```python
assign_db.add("assignments", {
    "name": "Group presentation",
    "module": "MK202",
    "owner": "huy",
    "days_left": 1,
    "difficulty": 5,
    "importance": 5,
    "completed": False,
    "score": 33
})
```

First argument is the list name inside the file (`"assignments"` or `"users"`), second is the dict to add. The DB assigns `id` automatically (don't pass one) and saves the file for you.

### query — read

```python
all_items = assign_db.query("assignments", [])
for a in all_items:
    print(a["name"], "-", a["days_left"], "days left")
```

The second argument is what you get back when nothing is found. Always pass `[]` when reading a list so the `for` loop never crashes.

### find — get one item

```python
a = assign_db.find("assignments", "id", 2)
if a:
    print(a["name"])
else:
    print("Not found")
```

Returns the first dict whose field matches, or `None`. Prefer searching by `"id"` — names can repeat, ids can't.

### update_where — modify one item

```python
assign_db.update_where("assignments", "id", 2, {"completed": True})
```

Finds the item with `id == 2` and overwrites the fields in the last dict. Fields you don't mention stay untouched. Returns `False` if nothing matched. Saves automatically.

### sort_by — rank

```python
top = assign_db.sort_by("assignments", "score", reverse=True, limit=5)
for i, a in enumerate(top, 1):
    print(f"{i}. {a['name']} ({a['score']} pts)")
```

`reverse=True` puts the highest score first. This powers the priority ranking feature.

## Putting it together: the StudySmart features

```python
from src.data_processing_module.config import assign_db

# Priority score formula — computed in the app layer; the DB never calculates it
def calc_score(days_left, difficulty, importance):
    urgency = max(1, 10 - days_left)
    return urgency * 2 + difficulty + importance * 2

# 1. Add an assignment
score = calc_score(3, 4, 5)
assign_db.add("assignments", {
    "name": "Python homework week 3", "module": "CS101", "owner": "huy",
    "days_left": 3, "difficulty": 4, "importance": 5,
    "completed": False, "score": score
})

# 2. View all
for a in assign_db.query("assignments", []):
    status = "done" if a["completed"] else "pending"
    print(a["id"], a["name"], status)

# 3. Priority ranking
top = assign_db.sort_by("assignments", "score", reverse=True, limit=5)

# 4. Mark as completed
assign_db.update_where("assignments", "id", 3, {"completed": True})

# 5. Study summary
items = assign_db.query("assignments", [])
done = [a for a in items if a["completed"]]
rate = len(done) / len(items) * 100 if items else 0
print(f"Completed {len(done)}/{len(items)} ({rate:.0f}%)")
```

## Users and passwords

Never store raw passwords — store a sha256 hex hash:

```python
import hashlib
from src.data_processing_module.config import users_db

def hash_pw(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

# Register — block duplicate usernames before adding
if users_db.find("users", "username", name):
    print("Username already exists")
else:
    users_db.add("users", {
        "username": name,
        "password_hash": hash_pw(pw),
        "role": "student"
    })

# Login
user = users_db.find("users", "username", name)
if user and user["password_hash"] == hash_pw(pw):
    print("Login successful")
```

Two common mistakes here: forgetting `.encode()` (crashes) and using `.digest()` instead of `.hexdigest()` (login silently fails every time).

Permissions live in the app layer, not the DB — the DB only stores the `role` field:

```python
if current_user.get("role") != "admin":
    print("You don't have permission for this")
```

Team note: this is honor-system permissioning. Anyone can open the JSON file in Notepad and change their role. Fine for a console project — just don't call it security in the docs.

## Mistakes beginners hit

- **Editing a dict and forgetting to save.** `find()` returns a reference; setting `a["completed"] = True` only changes RAM. Use `update_where` (saves for you), or call `assign_db.save(assign_db.data)` after manual edits.
- **`query` returns `None` and the `for` loop crashes.** Always pass `[]` as the default: `query("assignments", [])`.
- **`find` only returns the first match.** Search by `id`, not by `name`.
- **Editing the JSON file by hand while the app is running.** The app holds its own copy in RAM; the next save overwrites your manual change.
- **Running from the wrong directory.** Always `python -m src.cli_version.main` from the project root, or the path to `src/data/` breaks.
- **Broken JSON syntax** (missing comma, bad quotes) → `open()` prints "Error: The files format was not JSON". Paste the file into an online JSON validator to find the bad line.

## Quick reference

| Function | Job | Returns |
|---|---|---|
| `query(path, default)` | Read data by path | data or `default` |
| `find(list_key, field, value)` | Find one item | dict or `None` |
| `add(list_key, item)` | Add + auto-id + save | `True`/`None` |
| `update_where(list_key, field, value, updates)` | Modify + save | `True`/`False` |
| `sort_by(list_key, sort_key, reverse, limit)` | Rank items | list |
| `save(data)` | Write straight to file | `True`/`None` |
| `next_id()` | Generate a new id (add calls it for you) | int |