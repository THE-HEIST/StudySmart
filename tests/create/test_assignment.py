import pytest
from src.core.create.assignments import add_assignment
from datetime import datetime, timedelta
from src.data_processing_module.config4test import test_users_db as Users
from src.data_processing_module.config4test import test_assignments_db as Assignments

def test_add_assignment(monkeypatch):
    Assignments.clear_all("assignments")
    # Simulate user input for assignment details
    inputs = iter([
        "Test Assignment",  # Assignment name
        "Test Module",      # Module name
        "2024-12-31",       # Deadline
        "3"                 # Difficulty level
    ])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Call the function to add an assignment
    result = add_assignment(Assignments=Assignments)

    # Check if the function returns the expected status code
    assert result == True
    assert Assignments.find("assignments", "assignment_name", "Test Assignment") is not None

def test_add_assignment_invalid_difficulty(monkeypatch):
    Assignments.clear_all("assignments")
    # Simulate user input for assignment details with invalid difficulty level
    inputs = iter([
        "Test Assignment",  # Assignment name
        "Test Module",      # Module name
        "2024-12-31",       # Deadline
        "6",                # Invalid difficulty level (greater than 5)
        "0",                # Invalid difficulty level (less than 1)
        "3"                 # Valid difficulty level
    ])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Call the function to add an assignment
    result = add_assignment(Assignments=Assignments)

    # Check if the function returns the expected status code
    assert result == True
    assert Assignments.find("assignments", "assignment_name", "Test Assignment") is not None
