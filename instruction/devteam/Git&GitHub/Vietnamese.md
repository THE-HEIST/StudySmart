# Hướng dẫn Git & GitHub cho nhóm Studysmart

Mục tiêu: sau khi đọc xong, bạn code được trên branch riêng của mình, push/pull đúng chỗ, và tạo pull request để merge vào dự án. Không cần biết gì về Git trước.

## Git là gì, GitHub là gì

Git là công cụ lưu lịch sử code trên máy bạn — mỗi lần "commit" là một mốc lưu, quay lại được. GitHub là nơi chứa bản chung của cả nhóm trên mạng. Bạn kéo code từ GitHub về (`pull`), làm việc trên máy, rồi đẩy lên (`push`).

Quy tắc số một của nhóm: **không ai code trực tiếp trên branch `main`**. Mỗi người làm trên branch riêng, xong thì tạo pull request để nhóm review rồi mới merge vào `main`.

## Lần đầu tiên: cài đặt

Chỉ làm một lần trên máy của bạn.

```bash
# Khai bao ten va email (hien trong lich su commit)
git config --global user.name "Nguyen Van A"
git config --global user.email "email-cua-ban@gmail.com"

# Clone du an ve may
git clone https://github.com/<ten-org>/The-Black-Opal.git
cd The-Black-Opal
```

Nếu GitHub hỏi mật khẩu khi push: GitHub không nhận mật khẩu tài khoản nữa, phải dùng Personal Access Token. Vào GitHub → Settings → Developer settings → Personal access tokens → Generate new token (classic), tick quyền `repo`, rồi dán token đó vào ô mật khẩu. Lưu token lại vì nó chỉ hiện một lần.

## Vòng lặp làm việc hằng ngày

Đây là phần quan trọng nhất — thuộc 6 bước này là đủ làm việc nhóm.

### Bước 1: Cập nhật main mới nhất

Luôn bắt đầu từ main mới nhất, nếu không branch của bạn sẽ dựng trên code cũ:

```bash
git checkout main
git pull origin main
```

### Bước 2: Tạo branch riêng cho việc mình làm

```bash
git checkout -b feature/login
```

`-b` nghĩa là tạo mới rồi chuyển sang luôn. Đặt tên theo việc đang làm: `feature/login`, `feature/priority-ranking`, `fix/sort-bug`. Không dấu cách, không tiếng Việt có dấu.

Kiểm tra mình đang đứng ở branch nào:

```bash
git branch
# dau * la branch hien tai
```

### Bước 3: Code, rồi commit

Code như bình thường. Khi xong một phần có nghĩa (một hàm chạy được, một bug sửa xong), lưu mốc:

```bash
git status                       # xem file nao thay doi
git add src/core/login.py        # chon file muon luu
git add .                        # hoac chon tat ca
git commit -m "Them ham dang nhap voi hash sha256"
```

Message commit viết ngắn gọn, mô tả **làm gì**: "Them auto-increment id vao LangaDB", "Sua bug sort nguoc thu tu". Đừng viết "update", "fix bug", "abc" — hai tuần sau không ai hiểu.

Commit nhỏ và thường xuyên. Một commit khổng lồ "lam xong het" rất khó review và khó quay lui khi hỏng.

### Bước 4: Push branch lên GitHub

```bash
git push origin feature/login
```

Lần push đầu tiên của branch, Git có thể gợi ý lệnh dài hơn (`--set-upstream`) — cứ copy chạy theo, từ lần sau chỉ cần `git push`.

### Bước 5: Tạo pull request trên GitHub

1. Mở repo trên GitHub. Thường sẽ thấy banner vàng "feature/login had recent pushes" với nút **Compare & pull request** — bấm vào. Không thấy thì vào tab **Pull requests** → **New pull request**, chọn `base: main` ← `compare: feature/login`.
2. Đặt tiêu đề rõ ràng, viết vài dòng mô tả: làm gì, test chưa, có gì cần lưu ý.
3. Bấm **Create pull request**.
4. Nhắn nhóm review. Có góp ý thì sửa tiếp trên máy, commit và push lên branch cũ — PR tự cập nhật, không cần tạo PR mới.
5. Được duyệt thì bấm **Merge pull request** trên GitHub.

### Bước 6: Dọn dẹp sau khi merge

```bash
git checkout main
git pull origin main             # keo ban main da co code cua ban
git branch -d feature/login      # xoa branch cu tren may
```

Việc tiếp theo → quay lại Bước 1 với branch mới.

## Khi có conflict

Conflict xảy ra khi bạn và người khác cùng sửa một chỗ. GitHub sẽ báo "This branch has conflicts" trên PR. Cách xử lý trên máy:

```bash
git checkout feature/login
git pull origin main
```

Git sẽ báo file nào conflict. Mở file đó, bạn thấy:

```
<<<<<<< HEAD
    code cua ban
=======
    code cua nguoi kia
>>>>>>> main
```

Sửa lại đoạn đó thành phiên bản đúng cuối cùng (giữ của bạn, giữ của họ, hoặc gộp cả hai), **xóa hết 3 dòng ký hiệu** `<<<<<<<`, `=======`, `>>>>>>>`. Rồi:

```bash
git add .
git commit -m "Giai quyet conflict voi main"
git push origin feature/login
```

PR trên GitHub sẽ hết báo conflict. Không chắc nên giữ bên nào thì hỏi người viết đoạn kia — đừng đoán.

## Riêng cho dự án này

- **`session.txt` và `venv/` không được commit** — đã có trong `.gitignore`. Nếu `git status` vẫn thấy chúng, báo nhóm.
- **Cẩn thận với `users.json` và `assignments.json`**: chạy app là 2 file này đổi (dữ liệu test của bạn). Đừng `git add .` một cách vô thức rồi đẩy dữ liệu test của mình đè lên dummy data chung. Trước khi add, nhìn `git status`; muốn bỏ thay đổi của file dữ liệu:

```bash
git checkout -- src/data/assignments.json
```

- Mỗi PR nên gói gọn một tính năng. PR "làm login + sửa sort + đổi cấu trúc thư mục" sẽ bị trả về tách nhỏ.

## Cấp cứu

**Lỡ code trên main rồi (chưa commit):**

```bash
git checkout -b feature/ten-viec    # mang thay doi sang branch moi
```

Thay đổi đi theo bạn sang branch mới, main sạch trở lại.

**Lỡ commit lên main (chưa push):**

```bash
git checkout -b feature/ten-viec    # branch moi da chua commit do
git checkout main
git reset --hard origin/main        # keo main ve dung ban tren GitHub
```

**Muốn bỏ hết thay đổi chưa commit của một file:**

```bash
git checkout -- ten_file.py
```

Cẩn thận: mất thật, không hoàn tác được.

**Commit xong mới thấy sai message (chưa push):**

```bash
git commit --amend -m "Message dung"
```

**Đứng nhầm branch, muốn xem lại tình hình:**

```bash
git branch          # dang o dau
git status          # co gi chua commit
git log --oneline -5   # 5 commit gan nhat
```

Rối quá không gỡ được: đừng xóa thư mục dự án đi clone lại trong hoảng loạn — nhắn nhóm trước, đa số tình huống cứu được trong một phút.

## Bảng tra nhanh

| Lệnh | Việc |
|---|---|
| `git status` | Xem file nào đổi, đang ở branch nào |
| `git checkout main` + `git pull origin main` | Về main, cập nhật mới nhất |
| `git checkout -b feature/x` | Tạo branch mới và chuyển sang |
| `git add .` | Chọn thay đổi để commit |
| `git commit -m "..."` | Lưu mốc với message |
| `git push origin feature/x` | Đẩy branch lên GitHub |
| `git branch` | Liệt kê branch, đánh dấu branch hiện tại |
| `git log --oneline -5` | Xem lịch sử gần đây |