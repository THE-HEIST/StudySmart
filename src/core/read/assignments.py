from src.data_processing_module.config import Assignments

def view_order_by_undone(sort_key="score", reverse=True):
    db = Assignments.find("assignments", "completed", False)
    sorted_assignments = db.sort_by(sort_key=sort_key, reverse=reverse)
    return sorted_assignments

def view_order_by_done(sort_key="score", reverse=True):
    db = Assignments.find("assignments", "completed", True)
    sorted_assignments = db.sort_by(sort_key=sort_key, reverse=reverse)
    return sorted_assignments

# ==========================================
# FUNCTION 2: VIEW ASSIGNMENT
# ==========================================
def view_assignments(assignments):
    if len(assignments) == 0:
        print("No assignments found")
    else:
        header = ["ID", "Assignment Name", "Module", "Deadline", "Difficulty", "Score", "Completed"]
        print("{:<5} {:<20} {:<15} {:<12} {:<10} {:<8} {:<10}".format(*header))
        print("-" * 90)
        for assignment in assignments:
            row = [
                assignment.get("id", ""),
                assignment.get("assignment_name", ""),
                assignment.get("module_name", ""),
                assignment.get("deadline", ""),
                assignment.get("difficulty", ""),
                assignment.get("score", 0),
                "Done" if assignment.get("completed", True) else "Not Done"
            ]
            print("{:<5} {:<20} {:<15} {:<12} {:<10} {:<8} {:<10}".format(*row))