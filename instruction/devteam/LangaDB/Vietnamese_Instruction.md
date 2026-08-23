Hướng dẫn sử dụng LangaDB

LangaDB là lớp database mini của dự án The-Black-Opal. Nó lưu dữ liệu vào file JSON, đọc lên khi mở app, và ghi lại mỗi khi thêm/sửa. Không cần cài gì thêm — chỉ dùng `json` và `os` có sẵn trong Python.

Dự án dùng 2 file dữ liệu, nằm trong `src/data/`:

- `users.json` — tài khoản người dùng
- `assignments.json` — danh sách bài tập

## Bắt đầu nhanh

Không tự tạo `LangaDB(...)` mới trong code của bạn. Hai instance đã khởi tạo sẵn trong `config.py`, chỉ cần import:

```python
from src.data_processing_module.config import users_db, assign_db
```

Chạy app từ thư mục gốc dự án, dạng module:

```bash
python -m src.cli_version.main
```

Chạy kiểu `python src/cli_version/main.py` sẽ lỗi `ModuleNotFoundError: No module named 'src'`.

## Dữ liệu trong file trông thế nào

`assignments.json`:

```json
{
    "last_id": 2,
    "assignments": [
        {
            "id": 1,
            "name": "Bao cao AI",
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
            "name": "Essay Marketing",
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

`last_id` là bộ đếm để DB tự sinh `id` — đừng sửa tay. Mỗi item là một dict Python bình thường.

## Các hàm chính

### add — thêm mới

```python
assign_db.add("assignments", {
    "name": "Thuyet trinh nhom",
    "module": "MK202",
    "owner": "huy",
    "days_left": 1,
    "difficulty": 5,
    "importance": 5,
    "completed": False,
    "score": 33
})
```

Tham số đầu là tên list trong file (`"assignments"` hoặc `"users"`), tham số sau là dict cần thêm. DB tự gán `id` (không cần truyền) và tự lưu file luôn.

### query — lấy dữ liệu

```python
all_items = assign_db.query("assignments", [])
for a in all_items:
    print(a["name"], "-", a["days_left"], "ngay")
```

Tham số thứ hai là giá trị trả về khi không tìm thấy. Luôn truyền `[]` khi lấy list để vòng `for` không bị crash.

### find — tìm một item

```python
a = assign_db.find("assignments", "id", 2)
if a:
    print(a["name"])
else:
    print("Khong tim thay")
```

Trả về dict đầu tiên có field trùng giá trị, hoặc `None`. Ưu tiên tìm theo `"id"` — tên bài có thể trùng, id thì không.

### update_where — sửa một item

```python
assign_db.update_where("assignments", "id", 2, {"completed": True})
```

Tìm item có `id == 2` rồi ghi đè các field trong dict cuối. Field không nhắc tới giữ nguyên. Trả về `False` nếu không tìm thấy. Tự lưu file.

### sort_by — xếp hạng

```python
top = assign_db.sort_by("assignments", "score", reverse=True, limit=5)
for i, a in enumerate(top, 1):
    print(f"{i}. {a['name']} ({a['score']} diem)")
```

`reverse=True` → điểm cao đứng đầu. Đây là hàm dùng cho tính năng xếp hạng ưu tiên.

## Ví dụ ghép lại: các tính năng StudySmart

```python
from src.data_processing_module.config import assign_db

# Cong thuc diem uu tien — tinh o tang app, DB khong tu tinh
def calc_score(days_left, difficulty, importance):
    urgency = max(1, 10 - days_left)
    return urgency * 2 + difficulty + importance * 2

# 1. Them bai tap
score = calc_score(3, 4, 5)
assign_db.add("assignments", {
    "name": "Bai tap Python tuan 3", "module": "CS101", "owner": "huy",
    "days_left": 3, "difficulty": 4, "importance": 5,
    "completed": False, "score": score
})

# 2. Xem tat ca
for a in assign_db.query("assignments", []):
    trang_thai = "xong" if a["completed"] else "chua"
    print(a["id"], a["name"], trang_thai)

# 3. Xep hang uu tien
top = assign_db.sort_by("assignments", "score", reverse=True, limit=5)

# 4. Danh dau hoan thanh
assign_db.update_where("assignments", "id", 3, {"completed": True})

# 5. Thong ke
items = assign_db.query("assignments", [])
done = [a for a in items if a["completed"]]
rate = len(done) / len(items) * 100 if items else 0
print(f"Hoan thanh {len(done)}/{len(items)} ({rate:.0f}%)")
```

## User và mật khẩu

Mật khẩu không bao giờ lưu thô — lưu hash sha256 dạng hex:

```python
import hashlib
from src.data_processing_module.config import users_db

def hash_pw(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

# Dang ky — chan trung username truoc khi add
if users_db.find("users", "username", name):
    print("Username da ton tai")
else:
    users_db.add("users", {
        "username": name,
        "password_hash": hash_pw(pw),
        "role": "student"
    })

# Dang nhap
user = users_db.find("users", "username", name)
if user and user["password_hash"] == hash_pw(pw):
    print("Dang nhap thanh cong")
```

Hai lỗi hay gặp: quên `.encode()` (crash) và dùng `.digest()` thay vì `.hexdigest()` (login luôn sai mà không báo lỗi gì).

Phân quyền nằm ở tầng app, không nằm trong DB — DB chỉ lưu field `role`:

```python
if current_user.get("role") != "admin":
    print("Ban khong co quyen lam viec nay")
```

Lưu ý cho cả nhóm: đây là phân quyền kiểu tin nhau. Ai mở file JSON bằng Notepad cũng sửa được. Đủ cho project console, nhưng đừng gọi nó là bảo mật.

## Những lỗi người mới hay dính

- **Sửa dict rồi quên lưu.** `find()` trả về tham chiếu, sửa `a["completed"] = True` chỉ đổi trong RAM. Dùng `update_where` (tự lưu), hoặc gọi `assign_db.save(assign_db.data)` sau khi sửa tay.
- **`query` trả về `None` rồi `for` bị crash.** Luôn truyền default `[]`: `query("assignments", [])`.
- **`find` chỉ trả item đầu tiên trùng.** Tìm theo `id`, đừng tìm theo `name`.
- **Sửa file JSON bằng tay khi app đang chạy.** App giữ bản trong RAM; lần lưu tiếp theo sẽ ghi đè thay đổi tay của bạn.
- **Chạy sai thư mục.** Luôn `python -m src.cli_version.main` từ gốc dự án, nếu không đường dẫn tới `src/data/` sẽ lệch.
- **File JSON hỏng cú pháp** (thiếu dấu phẩy, quote sai) → `open()` in "Error: The files format was not JSON". Dán nội dung file vào một trình kiểm tra JSON online để tìm chỗ sai.

## Bảng tra nhanh

| Hàm | Việc | Trả về |
|---|---|---|
| `query(path, default)` | Lấy dữ liệu theo đường dẫn | dữ liệu hoặc `default` |
| `find(list_key, field, value)` | Tìm 1 item | dict hoặc `None` |
| `add(list_key, item)` | Thêm + tự gán id + lưu | `True`/`None` |
| `update_where(list_key, field, value, updates)` | Sửa + lưu | `True`/`False` |
| `sort_by(list_key, sort_key, reverse, limit)` | Xếp hạng | list |
| `save(data)` | Ghi thẳng ra file | `True`/`None` |
| `next_id()` | Sinh id mới (add gọi hộ rồi) | int |