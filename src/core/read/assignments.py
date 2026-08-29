from src.data_processing_module.config import Assignments
from src.core.authentication.session import load_session

def view_order_by_undone(sort_key="score", reverse=True, session=load_session()):
    db = Assignments.find("assignments", "user_id", session["user_id"])
    db = db.find("assignments", "completed", False)
    sorted_assignments = db.sort_by(sort_key=sort_key, reverse=reverse)
    return sorted_assignments

def view_order_by_done(sort_key="score", reverse=True, session=load_session()):
    db = Assignments.find("assignments", "user_id", session["user_id"])
    db = db.find("assignments", "completed", True)
    sorted_assignments = db.sort_by(sort_key=sort_key, reverse=reverse)
    return sorted_assignments

def view_order_all(sort_key="score", reverse=True, session=load_session()):
    db = Assignments.find("assignments", "user_id", session["user_id"])
    db = db.find("assignments", "completed", False) + db.find("assignments", "completed", True)
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

def show_study_summary(assignments):
    total_assignments = len(assignments)
    completed_count = 0
    incomplete_count = 0

    for assignment in assignments:
        if assignment["completed"]:
            completed_count = completed_count + 1
        else:
            incomplete_count = incomplete_count + 1

    if total_assignments == 0:
        completion_rate = 0
    else:
        completion_rate = (completed_count / total_assignments) * 100

    print("Total assignments:", total_assignments)
    print("Completed:", completed_count)
    print("Incomplete:", incomplete_count)
    print(f"Completion rate: {completion_rate}%")