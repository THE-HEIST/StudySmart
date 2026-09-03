from src.data_processing_module.config import Assignments, Users
from src.core.common.calculate_priority import *
from datetime import datetime, timedelta

# ==========================================
# FUNCTION 1: ADD ASSIGNMENT
# ==========================================
def add_assignment(Assignments=Assignments):
    # Prompt user to input information and loop to ensure them are not empty
    assignment_name = input("Assignment name:")
    while assignment_name == "":
          print("Assignment name cannot be empty!")
          assignment_name = input("Assignment name: ")

    module_name = input("Module:")
    while module_name == "":
           print("Module cannot be empty!")
           module_name = input("Module:")

    while True:
        try:
            deadline = input("Deadline (Ex: yyyy-mm-dd):")
            dl = datetime.strptime(deadline, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Invalid date format! Please enter the deadline in the format yyyy-mm-dd.")
    
    while True:
        try:
            difficulty = int(input("Difficulty level (1 to 5):"))
            while difficulty < 1 or difficulty > 5:
                print("---------------------")
                print("Please enter level from 1 to 5 !")
                print("---------------------")
                difficulty = int(input("Difficulty level:"))
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer for difficulty level.")

       # Validate that days remaining is within the valid range ( >0 )

    deadline = datetime.strptime(deadline, "%Y-%m-%d").date()

    # Generate unique assignment number based on current list length
    # Create dictionary containing all assignment details
    assignment = {
        "assignment_name": assignment_name,
        "module_name": module_name,
        "deadline": deadline.strftime("%Y-%m-%d"),
        "difficulty": difficulty,
        "completed": False,
    }
    assignment["score"] = calculate_priority_score(assignment)
    assignment["level"] = get_priority_level(assignment["score"])
    # Append the newly created assignment record to the main list
    Assignments.add("assignments", assignment)

    return True