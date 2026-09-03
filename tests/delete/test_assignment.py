from src.core.delete.assignment import delete_assignment
import pytest
from src.data_processing_module.config4test import test_assignments_db as Assignments

def test_delete_assignment(monkeypatch):
    # Create a mock assignment to delete
    mock_assignment = {
        "id": 1,
        "title": "Test Assignment",
        "description": "This is a test assignment.",
        "priority": 1,
        "status": "undone"
    }
    
    # Save the mock assignment to the Assignments
    Assignments.save({"last_id": 1, "assignments": [mock_assignment]})
    
    # Call the delete_assignment function
    inputs = iter(["1"])  # Simulate user input for assignment number to delete
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    delete_assignment(Assignments=Assignments, assignments=Assignments.all("assignments"))

    
    # Verify that the assignment has been deleted
    assignments = Assignments.all("assignments")
    assert len(assignments) == 0