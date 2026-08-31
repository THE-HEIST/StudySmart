from src.core.read.assignments import view_assignments
from src.data_processing_module.config import Assignments

def delete_assignment(Assignments=Assignments, assignments=None):
    if assignments is None or len(assignments) == 0:
        print("\nNo assignments to delete.\n")
        return

    view_assignments(assignments=assignments)

    user_input = input("\nEnter the assignment number to delete: ")
    if not user_input.isdigit():
        error_message = "\nInvalid selection. Please choose a valid assignment number.\n"
        print(error_message)
        return

    selected_number = int(user_input)
    ass = Assignments.find("assignments", "id", selected_number)

    if (selected_number >= 0 and ass is not None):
        Assignments.delete("assignments", "id", selected_number)
        print("\nAssignment deleted successfully.\n")
    else:
       error_message = "\nInvalid selection. Please choose a valid assignment number.\n"
       print(error_message)