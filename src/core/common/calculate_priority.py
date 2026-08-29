from datetime import datetime, timedelta

def calculate_priority_score(assignment):
    difficulty = int(assignment["difficulty"])
    #date = datetime.strptime(assignment["deadline"], "%Y-%m-%d")
    date_now = datetime.now().date()
    days_remaining = int((datetime.strptime(assignment['deadline'], "%Y-%m-%d").date() - date_now).days)
    if days_remaining < 0:
        priority_score = 99999
    else:
        priority_score = difficulty / (days_remaining + 1)
    return priority_score

def get_priority_level(priority_score):
    if priority_score == 99999:
        priority_level = "OVERDUE"
    elif priority_score >= 2:
        priority_level = "HIGH"
    elif priority_score < 1:
        priority_level = "LOW"
    else:
        priority_level = "MEDIUM"
    return priority_level

"""
def view_priority_ranking(assignments):
    unfinished_assignments = []
    for assignment in assignments:
        if assignment["completed"] == False:
            unfinished_assignments.append (assignment)
    if unfinished_assignments == []:
        print ("Không có danh Task nào chưa hoàn thành")
        return unfinished_assignments
    ranked_assignments = sorted(unfinished_assignments , key= calculate_priority_score, reverse=True)
    for assignment_number, assignment in enumerate(ranked_assignments, start=1):
        priority_score = calculate_priority_score(assignment)
        priority_level = get_priority_level (priority_score)
        assignment_name = assignment["assignment_name"]
        print (assignment_number, assignment_name, priority_score, priority_level)
    return ranked_assignments
"""

def re_calculate_priority(assignments):
    for assignment in assignments:
        priority_score = calculate_priority_score(assignment)
        priority_level = get_priority_level(priority_score)
        assignment["priority_score"] = priority_score
        assignment["priority_level"] = priority_level
    return assignments