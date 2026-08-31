from src.data_processing_module.config import Assignments
from src.core.authentication.session import load_session

def view_order_by_undone(Assignments=Assignments, sort_key="score", reverse=True, session=None):
    if session is None:
        session = load_session()
    all_assignments = Assignments.query("assignments", []) if hasattr(Assignments, "query") else (Assignments if isinstance(Assignments, list) else [])
    if not isinstance(all_assignments, list):
        all_assignments = []
    user_id = session.get("id") if isinstance(session, dict) else None
    if user_id is not None:
        filtered = [a for a in all_assignments if (a.get("user_id") is None or a.get("user_id") == user_id) and not a.get("completed")]
    else:
        filtered = [a for a in all_assignments if not a.get("completed")]
    return sorted(filtered, key=lambda x: x.get(sort_key, 0), reverse=reverse)

def view_order_by_done(Assignments=Assignments, sort_key="score", reverse=True, session=None):
    if session is None:
        session = load_session()
    all_assignments = Assignments.query("assignments", []) if hasattr(Assignments, "query") else (Assignments if isinstance(Assignments, list) else [])
    if not isinstance(all_assignments, list):
        all_assignments = []
    user_id = session.get("id") if isinstance(session, dict) else None
    if user_id is not None:
        filtered = [a for a in all_assignments if (a.get("user_id") is None or a.get("user_id") == user_id) and a.get("completed")]
    else:
        filtered = [a for a in all_assignments if a.get("completed")]
    return sorted(filtered, key=lambda x: x.get(sort_key, 0), reverse=reverse)

def view_order_all(Assignments=Assignments, sort_key="score", reverse=True, session=None):
    if session is None:
        session = load_session()
    all_assignments = Assignments.query("assignments", []) if hasattr(Assignments, "query") else (Assignments if isinstance(Assignments, list) else [])
    if not isinstance(all_assignments, list):
        all_assignments = []
    user_id = session.get("id") if isinstance(session, dict) else None
    if user_id is not None:
        filtered = [a for a in all_assignments if a.get("user_id") is None or a.get("user_id") == user_id]
    else:
        filtered = list(all_assignments)
    return sorted(filtered, key=lambda x: x.get(sort_key, 0), reverse=reverse)

# ==========================================
# FUNCTION 2: VIEW ASSIGNMENT
# ==========================================
def view_assignments(Assignments=Assignments, assignments=None):
    if isinstance(Assignments, list) and assignments is None:
        assignments = Assignments
        Assignments = None
    elif assignments is None:
        if hasattr(Assignments, "all"):
            assignments = Assignments.all("assignments")
        elif hasattr(Assignments, "query"):
            assignments = Assignments.query("assignments", [])
        else:
            assignments = []
    
    if len(assignments) == 0:
        print("No assignments found")
    else:
        header = ["ID", "Assignment Name", "Module", "Deadline", "Difficulty", "Score", "Completed"]
        print("{:<5} {:<20} {:<15} {:<12} {:<15} {:<8} {:<10}".format(*header))
        print("-" * 90)
        for assignment in assignments:
            row = [
                assignment.get("id", ""),
                assignment.get("assignment_name", ""),
                assignment.get("module_name", ""),
                assignment.get("deadline", ""),
                assignment.get("difficulty", ""),
                round(assignment.get("score", 0), 2),
                "Done" if assignment.get("completed", True) else "Not Done"
            ]
            print("{:<5} {:<20} {:<15} {:<12} {:<15} {:<8} {:<10}".format(*row))

def show_study_summary(assignments):
    total_assignments = len(assignments)
    completed_count = 0
    incomplete_count = 0

    for assignment in assignments:
        if assignment.get("completed"):
            completed_count = completed_count + 1
        else:
            incomplete_count = incomplete_count + 1

    if total_assignments == 0:
        completion_rate = 0
    else:
        completion_rate = round((completed_count / total_assignments) * 100, 2)

    print("Total assignments:", total_assignments)
    print("Completed:", completed_count)
    print("Incomplete:", incomplete_count)
    print(f"Completion rate: {completion_rate}%")
from src.data_processing_module.config import Assignments
from src.core.authentication.session import load_session

def view_order_by_undone(Assignments=Assignments, sort_key="score", reverse=True, session=None):
    assignments = Assignments.all('assignments')
    a = []
    for i in assignments:
        if i.get("completed") == False:
            a.append(i)
    return sorted(assignments, key=lambda x: x[sort_key], reverse=reverse)

def view_order_by_done(Assignments=Assignments, sort_key="score", reverse=True, session=None):
    assignments = Assignments.all('assignments')
    a = []
    for i in assignments:
        if i.get("completed") == True:
            a.append(i)
    return sorted(assignments, key=lambda x: x.get(sort_key,0),reverse=reverse)

def view_order_all(Assignments=Assignments, sort_key="score", reverse=True, session=None):
    assignments = Assignments.all('assignments')
    return sorted(assignments, key=lambda x: x.get(sort_key,0), reverse=reverse)

# ==========================================
# FUNCTION 2: VIEW ASSIGNMENT
# ==========================================
def view_assignments(Assignments=Assignments, assignments=None):
    """
    if isinstance(Assignments, list) and assignments is None:
        assignments = Assignments
        Assignments = None
    elif assignments is None:
        if hasattr(Assignments, "all"):
            assignments = Assignments.all("assignments")
        elif hasattr(Assignments, "query"):
            assignments = Assignments.query("assignments", [])
        else:
            assignments = []
    """
    
    if len(assignments) == 0 or assignments == None:
        print("No assignments found")
    else:
        header = ["ID", "Assignment Name", "Module", "Deadline", "Difficulty", "Score", "Completed"]
        print("{:<5} {:<20} {:<15} {:<12} {:<15} {:<8} {:<10}".format(*header))
        print("-" * 90)
        for assignment in assignments:
            row = [
                assignment.get("id", ""),
                assignment.get("assignment_name", ""),
                assignment.get("module_name", ""),
                assignment.get("deadline", ""),
                assignment.get("difficulty", ""),
                round(assignment.get("score", 0), 2),
                "Done" if assignment.get("completed", True) else "Not Done"
            ]
            print("{:<5} {:<20} {:<15} {:<12} {:<15} {:<8} {:<10}".format(*row))

def show_study_summary(assignments):
    total_assignments = len(assignments)
    completed_count = 0
    incomplete_count = 0

    for assignment in assignments:
        if assignment.get("completed"):
            completed_count = completed_count + 1
        else:
            incomplete_count = incomplete_count + 1

    if total_assignments == 0:
        completion_rate = 0
    else:
        completion_rate = round((completed_count / total_assignments) * 100, 2)

    print("Total assignments:", total_assignments)
    print("Completed:", completed_count)
    print("Incomplete:", incomplete_count)
    print(f"Completion rate: {completion_rate}%")