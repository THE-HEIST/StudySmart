from src.update.mark_as_done import mark_completed, undo_mark_as_done
import pytest
from src.data_processing_module.config4test import test_assignment_db as Assignments

def test_mark_completed():
    # Clear the assignments before testing
    Assignments.clear_all("assignments")
    
    # Add a test assignment
    Assignments.add("assignments", {"id": 1, "assignment_name": "Test Assignment", "completed": False})
    
    # Simulate user input for marking the assignment as completed
    def mock_input(prompt):
        return "1"  # User selects the first assignment
    
    # Replace the built-in input function with our mock_input
    original_input = __builtins__.input
    __builtins__.input = mock_input
    
    try:
        # Call the mark_completed function
        mark_completed(Assignments=Assignments, assignments=[{"id": 1, "assignment_name": "Test Assignment", "completed": False}])
        
        # Check if the assignment is marked as completed
        updated_assignment = Assignments.find("assignments", "id", 1)
        assert updated_assignment["completed"] == True
    finally:
        # Restore the original input function
        __builtins__.input = original_input

def test_undo_mark_as_done():
    # Clear the assignments before testing
    Assignments.clear_all("assignments")
    
    # Add a test assignment marked as completed
    Assignments.add("assignments", {"id": 1, "assignment_name": "Test Assignment", "completed": True})
    
    # Simulate user input for undoing the mark as completed
    def mock_input(prompt):
        return "1"  # User selects the first assignment
    
    # Replace the built-in input function with our mock_input
    original_input = __builtins__.input
    __builtins__.input = mock_input
    
    try:
        # Call the undo_mark_as_done function
        undo_mark_as_done(Assignments=Assignments, assignments=[{"id": 1, "assignment_name": "Test Assignment", "completed": True}])
        
        # Check if the assignment is marked as not completed
        updated_assignment = Assignments.find("assignments", "id", 1)
        assert updated_assignment["completed"] == False
    finally:
        # Restore the original input function
        __builtins__.input = original_input
    