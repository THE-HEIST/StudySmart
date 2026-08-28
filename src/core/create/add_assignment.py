# Initialize an empty list to store assignment dictionaries
assignments = []
# ==========================================
# FUNCTION 1: ADD ASSIGNMENT
# ==========================================
def add_assignment(assignments):
    # Prompt user to input information and loop to ensure them are not empty
    assignment_name = input("Assignment name:")
    while assignment_name == "":
          print("Assignment name cannot be empty!")
          assignment_name = input("Assignment name: ")
    module_name = input("Module:")
    while module_name == "":
           print("Module cannot be empty!")
           module_name = input("Module:")
    days_remaining = int(input("Days remaining:"))
    while days_remaining == "":
           print("Days remaining cannot be empty!")
           days_remaining = int(input("Days remaining:"))
    difficulty = int(input("Difficulty level (1 to 5):"))
    while difficulty == "":
           print("Difficulty level cannot be empty!")
           difficulty = int(input("Difficulty level (1 to 5):"))

       # Validate that days remaining is within the valid range ( >0 )
    while days_remaining < 0 :
               print("---------------------")
               print("Please enter a positive number !")
               print("---------------------")
               days_remaining = int(input("Days remaining:"))

    # Validate that difficulty level is within the valid range (1 to 5)
    while difficulty < 1 or difficulty > 5:
        print("---------------------")
        print("Please enter level from 1 to 5 !")
        print("---------------------")
        difficulty = int(input("Difficulty level:"))

    # Generate unique assignment number based on current list length
    assignment_number = len(assignments) + 1
    # Create dictionary containing all assignment details
    assignment = {
        "assignment_number": assignment_number,
        "assignment_name": assignment_name,
        "module_name": module_name,
        "days_remaining": days_remaining,
        "difficulty": difficulty,
        "completed": False
    }
    # Append the newly created assignment record to the main list
    assignments.append(assignment)