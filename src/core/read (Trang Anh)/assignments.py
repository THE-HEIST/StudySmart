from src.data_processing_module.config import Assignments

def view_order_by_undone(sort_key="score", reverse=True, limit=5):
    db = Assignments.find("assignments", "completed", False)
    sorted_assignments = db.sort_by(sort_key=sort_key, reverse=reverse, limit=limit)
    return sorted_assignments

def view_order_by_done(sort_key="score", reverse=True, limit=5):
    db = Assignments.find("assignments", "completed", True)
    sorted_assignments = db.sort_by(sort_key=sort_key, reverse=reverse, limit=limit)
    return sorted_assignments