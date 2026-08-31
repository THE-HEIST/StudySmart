from src.data_processing_module.config import Assignments
from src.core.read.assignments import view_assignments
from src.core.common.calculate_priority import calculate_priority_score

def update_assignment(assignments=None, Assignments = Assignments):
    if len(assignments) == 0:
        print("\nNo assignments to update.\n")
        return

<<<<<<< HEAD
    view_assignments(assignments=assignments)
=======
    view_assignments(assignments)
>>>>>>> a524f49cccca3ba2298e5f8411e810d123d52f66

    user_input = input("\nEnter the assignment number to update: ")
    if not user_input.isdigit():
        error_message = "\nInvalid selection. Please choose a valid assignment number.\n"
        print(error_message)
        return

    selected_number = int(user_input)
    selected_index = selected_number - 1

    if selected_index >= 0 and selected_index < len(assignments):
        assignment_to_update = assignments[selected_index]
        print(f"\nUpdating assignment: {assignment_to_update.get('assignment_name')}\n")

        new_name = input("Enter new assignment name (leave blank to keep current): ")
        new_module = input("Enter new module name (leave blank to keep current): ")
        new_deadline = input("Enter new deadline (leave blank to keep current): ")
        new_difficulty = input("Enter new difficulty (leave blank to keep current): ")
        #new_score = input("Enter new score (leave blank to keep current): ")

        if new_name:
            Assignments.update("assignments", "id", assignment_to_update["id"], {"assignment_name": new_name})
        if new_module:
            Assignments.update("assignments", "id", assignment_to_update["id"], {"module_name": new_module})
        if new_deadline:
            Assignments.update("assignments", "id", assignment_to_update["id"], {"deadline": new_deadline})
        if new_difficulty:
            Assignments.update("assignments", "id", assignment_to_update["id"], {"difficulty": int(new_difficulty)})
        #if new_score:
        #
        #    Assignments.update("assignments", "id", assignment_to_update["id"], {"score": int(new_score)})

        Assignments.update('assignments','score', assignment_to_update['id'], {'score': calculate_priority_score(Assignments.find('assignments','id', assignment_to_update['id']))})

        print("\nAssignment updated successfully.\n")
    else:
        error_message = "\nInvalid selection. Please choose a valid assignment number.\n"
        print(error_message)