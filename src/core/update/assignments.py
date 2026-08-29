from src.data_processing_module.config import Assignments
from src.core.read.assignments import view_assignments

def update_assignment(assignments=None, Assignments = Assignments):
    if len(assignments) == 0:
        print("No assignments to update.")
        return

    view_assignments(assignments)

    user_input = input("Enter the assignment number to update: ")
    if not user_input.isdigit():
        error_message = "Invalid selection. Please choose a valid assignment number."
        print(error_message)
        return

    selected_number = int(user_input)
    selected_index = selected_number - 1

    if selected_index >= 0 and selected_index < len(assignments):
        assignment_to_update = assignments[selected_index]
        print("Updating assignment:", assignment_to_update["assignment_name"])

        new_name = input("Enter new assignment name (leave blank to keep current): ")
        new_module = input("Enter new module name (leave blank to keep current): ")
        new_deadline = input("Enter new deadline (leave blank to keep current): ")
        new_difficulty = input("Enter new difficulty (leave blank to keep current): ")
        new_score = input("Enter new score (leave blank to keep current): ")

        if new_name:
            #assignment_to_update["assignment_name"] = new_name
            Assignments.update("assignments", "id", assignment_to_update["id"], {"assignment_name": new_name})
        if new_module:
            #assignment_to_update["module_name"] = new_module
            Assignments.update("assignments", "id", assignment_to_update["id"], {"module_name": new_module})
        if new_deadline:
            #assignment_to_update["deadline"] = new_deadline
            Assignments.update("assignments", "id", assignment_to_update["id"], {"deadline": new_deadline})
        if new_difficulty:
            #assignment_to_update["difficulty"] = int(new_difficulty)
            Assignments.update("assignments", "id", assignment_to_update["id"], {"difficulty": int(new_difficulty)})
        if new_score:
            #assignment_to_update["score"] = int(new_score)
            Assignments.update("assignments", "id", assignment_to_update["id"], {"score": int(new_score)})

        print("Assignment updated successfully.")
    else:
        error_message = "Invalid selection. Please choose a valid assignment number."
        print(error_message)