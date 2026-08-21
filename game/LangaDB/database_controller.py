import json
import os

class LangaDB:
    def __init__(self, db_path, default_data):
        self.db_path = db_path
        #self.db_type = db_type
        self.data = default_data if default_data is not None else {}
        self.open()

    def open(self):
        if not os.path.exists(self.db_path):
            try:
                with open(self.db_path, "x", encoding='utf-8') as file:
                    file.write("[]" if isinstance(self.data, list) else "{}")
            except FileExistsError:
                print("The file already exists. No changes were made.")
        else:
            try:
                with open(self.db_path, 'r', encoding='utf-8') as file:
                    self.data = json.loads(file.read())
            except json.JSONDecodeError:
                print("Error: The files format was not JSON")
                return False
            except Exception as e:
                print(f"Error: {e}")
                return False

    def query_all(self, name):
        return self.data.get('name')

    def save(self, new_data):
        try:
            with open(self.db_path, 'w', encoding='utf-8') as file:
                json.dump(new_data, file, ensure_ascii=False, indent=4)
            return True
        except Exception as e:
            print(f"Error: {e}")

    def query(self, path, default=None):
        keys = path.split('.')
        current = self.data

        for key in keys:
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                return default
        return current

    def find(self, list_key, field_name,value):
        items = self.query(list_key, [])
        if isinstance(items, list):
            for item in items:
                if isinstance(item,dict) and items.get(field_name) == value:
                    return item
        return None

    def add(self, list_key, new_items):
        target = self.query(list_key)
        if isinstance(target,list):
            target.append(new_items)
        elif self.data == [] or isinstance(self.data, list):
            self.data.append(new_items)
        return self.save_data()

    def sort_by(self, sort_key="score",reverse=True, limit=5):
        items = self.data if isinstance(self.data, list) else self.query("",[])
        if not isinstance(items, list):
            return []
        result = sorted(items,key=lambda item: item.get(sort_key, 0))
        return result[:limit]

    def _check_condition(self, item, field_name, value, operator):
        if not isinstance(item, dict) or field_name not in item:
            return False
            
        field_val = item[field_name]
        try:
            if operator == "eq": return field_val == value
            elif operator == "neq": return field_val != value
            elif operator == "gt": return field_val > value
            elif operator == "gte": return field_val >= value
            elif operator == "lt": return field_val < value
            elif operator == "lte": return field_val <= value
            elif operator == "contains":
                return isinstance(field_val, (str, list)) and value in field_val
            elif operator == "in":
                return isinstance(value, (list, tuple, set)) and field_val in value
        except TypeError:
            return False
        return False

    def paginate(self, data_list, page=1, page_size=10):
        if not isinstance(data_list, list):
            data_list = []

        # Đảm bảo page và page_size hợp lệ (tối thiểu là 1)
        page = max(1, int(page))
        page_size = max(1, int(page_size))

        total_items = len(data_list)
        total_pages = (total_items + page_size - 1) // page_size if total_items > 0 else 1

        # Tính toán offset
        offset = (page - 1) * page_size
        items = data_list[offset : offset + page_size]

        return {
            "items": items,
            "pagination": {
                "total_items": total_items,
                "total_pages": total_pages,
                "current_page": page,
                "page_size": page_size,
                "has_next": page < total_pages,
                "has_prev": page > 1,
                "offset": offset
            }
        }

    def filter(self, list_key, conditions, match_type="AND", page=None, page_size=10):
        if isinstance(conditions, tuple):
            conditions = [conditions]

        items = self.query(list_key, []) if list_key else self.data
        if not isinstance(items, list):
            return self.paginate([], page, page_size) if page is not None else []

        results = []
        for item in items:
            if match_type.upper() == "AND":
                if all(self._check_condition(item, field, val, op) for field, op, val in conditions):
                    results.append(item)
            elif match_type.upper() == "OR":
                if any(self._check_condition(item, field, val, op) for field, op, val in conditions):
                    results.append(item)

        # Nếu có truyền tham số page thì tự động phân trang kết quả lọc
        if page is not None:
            return self.paginate(results, page=page, page_size=page_size)

        return results

    def update(self, list_key, field_name, value, new_data):
        """CẬP NHẬT: Cập nhật thông tin của phần tử khớp điều kiện."""
        items = self.query(list_key, []) if list_key else self.data
        if isinstance(items, list):
            for item in items:
                if isinstance(item, dict) and item.get(field_name) == value:
                    item.update(new_data)
                    return self.save()
        return False

    def delete(self, list_key, field_name, value):
        """XÓA: Xóa phần tử khớp điều kiện khỏi danh sách."""
        items = self.query(list_key, None) if list_key else self.data
        if isinstance(items, list):
            for i, item in enumerate(items):
                if isinstance(item, dict) and item.get(field_name) == value:
                    items.pop(i)
                    return self.save()
        return False