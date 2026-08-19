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
                with open(self.db_path, 'x', encoding='utf-8') as file:
                    file.write("[]" if isinstance(self.data, list) else "{}")
            except Exception as e:
                print(f"Error: {e}")
                return False
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
        return self.data.get(name)

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
                if isinstance(item,dict) and item.get(field_name) == value:
                    return item
        return None

    def auto_increment_id(self, counter_key="last_id"):
        current = self.data.get(counter_key, 0) if isinstance(self.data, dict) else 0
        new_id = current + 1
        if isinstance(self.data, dict):
            self.data[counter_key] = new_id
        return new_id

    def add(self, list_key, new_item, auto_id=True):
        if auto_id and isinstance(new_item, dict) and "id" not in new_item:
            new_item["id"] = self.next_id()
        target = self.query(list_key)
        if isinstance(target, list):
            target.append(new_item)
        elif self.data == [] or isinstance(self.data, list):
            self.data.append(new_item)
        return self.save(self.data)

    def sort_by(self, list_key="assignments", sort_key="score",reverse=True, limit=5):
        items = self.data if isinstance(self.data, list) else self.query(list_key, self.data if isinstance(self.data, list) else [])
        if not isinstance(items, list):
            return []
        result = sorted(items,key=lambda item: item.get(sort_key, 0), reverse=reverse)
        return result[:limit]

    def update_where(self, list_key, field_name, value, updates):
        item = self.find(list_key, field_name, value)
        if item:
            item.update(updates)
            return self.save(self.data)
        return False