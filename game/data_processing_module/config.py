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
            print("Error: The files does not exist")
            return False
        try:
            with open(self.db_path, 'r', encoding='utf-8') as file:
                self.data = json.loads(file.read())
        except json.JSONDecodeError:
            print("Error: The files format was not JSON")
            return False
        except Exception as e:
            print(f"Error: {e}")
            return False

    def get_all_data(self, name):
        return self.data.get('name')

    def save_data(self, new_data):
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

    def find_where(self, list_key, field_name,value):
        items = self.query(list_key, [])
        if isinstance(items, list):
            for item in items:
                if isinstance(item,dict) and items.get(field_name) == value:
                    return item
        return None

    def push_to_list(self, list_key, new_items):
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