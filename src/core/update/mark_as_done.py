from src.data_processing_module.config import Assignments
from src.core.read.assignments import view_assignments

def mark_completed(Assignments=Assignments, assignments=None):
    if assignments is None or len(assignments) == 0:
        print("\nNo assignments to update.\n")
        return

    view_assignments(assignments)

    user_input = input("\nEnter the assignment number to mark as completed: ")
    if not user_input.isdigit():
        error_message = "\nInvalid selection. Please choose a valid assignment number.\n"
        print(error_message)
        return

    selected_number = int(user_input)
    ass = Assignments.find("assignments", "id", selected_number)

    if (selected_number >= 0 and ass is not None and ass['completed'] == False):
        Assignments.update("assignments", "id", selected_number, {"completed": True})
        print("\nAssignment marked as completed.\n")
    else:
       error_message = "\nInvalid selection. Please choose a valid assignment number.\n"
       print(error_message)

def undo_mark_as_done(Assignments=Assignments, assignments=None):
    if assignments is None or len(assignments) == 0:
        print("\nNo assignments to update.\n")
        return

    view_assignments(assignments)

    user_input = input("\nEnter the assignment number to undo mark as completed: ")
    if not user_input.isdigit():
        error_message = "\nInvalid selection. Please choose a valid assignment number.\n"
        print(error_message)
        return

    selected_number = int(user_input)
    ass = Assignments.find("assignments", "id", selected_number)

    if (selected_number >= 0  and ass is not None and ass['completed'] == True):
        Assignments.update("assignments", "id", selected_number, {"completed": False})
        print("\nAssignment marked as not completed.\n")
    else:
       error_message = "\nInvalid selection. Please choose a valid assignment number.\n"
       print(error_message)