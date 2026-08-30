from src.core.update.assignments import update_assignment
from src.data_processing_module.config4test import test_assignments_db as Assignments
import pytest

def test_update_assignment(monkeypatch):
    # Clear the assignments before testing
    Assignments.clear_all("assignments")
    
    # Add a test assignment
    Assignments.add("assignments", {"id": 1, "assignment_name": "Test Assignment", "module_name": "Test Module", "deadline": "2024-12-31", "difficulty": 3, "score": 5, "completed": False, 'user_id':1})
    
    # Simulate user input for updating the assignment
    """
    def mock_input(prompt):
        if "Enter the ID of the assignment" in prompt:
            return "1"  # User selects the first assignment
        elif "Enter new assignment name" in prompt:
            return "Updated Assignment"
        elif "Enter new module name" in prompt:
            return "Updated Module"
        elif "Enter new deadline" in prompt:
            return "2025-01-31"
        elif "Enter new difficulty" in prompt:
            return "4"
        elif "Enter new score" in prompt:
            return "10"
        else:
            return ""
    
    # Replace the built-in input function with our mock_input
    original_input = __builtins__.input
    __builtins__.input = mock_input
    """

    inputs = iter([
        "1",  # User selects the first assignment
        "Updated Assignment",  # New assignment name
        "Updated Module",      # New module name
        "2025-01-31",          # New deadline
        "4",                   # New difficulty                   # New score
    ])
    original_input = monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    # Call the update_assignment function
    update_assignment(Assignments=Assignments, assignments=[{"id": 1, "assignment_name": "Test Assignment", "module_name": "Test Module", "deadline": "2024-12-31", "difficulty": 3, "score": 5, "completed": False, 'user_id':1}])
        
    # Check if the assignment is updated correctly
    updated_assignment = Assignments.find("assignments", "id", 1)
    assert updated_assignment["assignment_name"] == "Updated Assignment"
    assert updated_assignment["module_name"] == "Updated Module"
    assert updated_assignment["deadline"] == "2025-01-31"
    assert updated_assignment["difficulty"] == 4
    assert updated_assignment["score"] == 5