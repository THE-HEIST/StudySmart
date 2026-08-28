# ==========================================
# FUNCTION 2: VIEW ASSIGNMENT
# ==========================================
def view_assignments(assignments):
    # Check if assignment list is empty and display message
    if len(assignments) == 0:
        print("No assignments found")
    for assignment in assignments:
        # Check if the assignment is marked as completed
        if assignment["completed"] == True:
            print(f"""--Assignment name: {assignment["assignment_number"]}.{assignment["assignment_name"]} \nModule: {assignment["module_name"]} \nDays remaining: {assignment["days_remaining"]} \nDifficulty level: {assignment["difficulty"]}\nStatus: Done--""")
        else:
            print(f"""--Assignment name: {assignment["assignment_number"]}.{assignment["assignment_name"]} \nModule: {assignment["module_name"]} \nDays remaining: {assignment["days_remaining"]} \nDifficulty level: {assignment["difficulty"]}\nStatus: Not done--""")