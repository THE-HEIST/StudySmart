from src.data_processing_module.config import Assignments
from src.core.read.assignments import view_assignments

def mark_completed(Assigments=Assignments, assignments=None):
    if len(assignments) == 0:
        print("No assignments to update.")
        return

    view_assignments(assignments)

    """
    for i in range (len(assignments)):
        assignment_number = i + 1
        if assignments[i]["completed"]:
            status_text = "Completed"
        else:
            status_text = "Incomplete"
        print(f"{assignment_number}. {assignments[i]['assignment_name']} - {status_text}")
    """

    user_input = input("Enter the assignment number to mark as completed: ")
    if not user_input.isdigit():
        error_message = "Invalid selection. Please choose a valid assignment number."
        print(error_message)
        return

    selected_number = int(user_input)
    #selected_index = selected_number - 1
    ass = Assignments.find("assignments", "id", selected_number)

    if (selected_index >= 0 and selected_index < len(assignments) and ass is not None and ass['completed'] == False):
        Assignments.update("assignments", "id", selected_number, {"completed": True})
        print("Assignment marked as completed.")
    else:
       error_message = "Invalid selection. Please choose a valid assignment number."
       print(error_message)

def undo_mark_as_done(Assigments=Assignments, assignments=None):
    if len(assignments) == 0:
        print("No assignments to update.")
        return

    view_assignments(assignments)

    user_input = input("Enter the assignment number to undo mark as completed: ")
    if not user_input.isdigit():
        error_message = "Invalid selection. Please choose a valid assignment number."
        print(error_message)
        return

    selected_number = int(user_input)
    #selected_index = selected_number - 1
    ass = Assignments.find("assignments", "id", selected_number)

    if (selected_index >= 0 and selected_index < len(assignments) and ass is not None and ass['completed'] == True):
        #ass = Assignments.find("assignments", "id", selected_number)
        Assignments.update("assignments", "id", selected_number, {"completed": True})
        print("Assignment marked as not completed.")
    else:
       error_message = "Invalid selection. Please choose a valid assignment number."
       print(error_message)