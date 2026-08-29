import pytest
from src.core.create.assignments import add_assignment
from datetime import datetime
from src.data_processing_module.config4test import test_assignments_db as Assignments

Assignments.clear_all("assignments")

"""
assignment = [{
    "id": 1,
    "assignment_name": "assignment_name",
    "module_name": "module_name",
    "deadline": datetime.date.today().strftime("%Y-%m-%d") + datetime.timedelta(days=1).strftime("%Y-%m-%d"),
    "difficulty": 4,
    "score": 0,
    "user_id": 1,
    "completed": True
},{
    "id": 2,
    "assignment_name": "assignment_name",
    "module_name": "module_name",
    "deadline": datetime.date.today().strftime("%Y-%m-%d") + datetime.timedelta(days=1).strftime("%Y-%m-%d"),
    "difficulty": 2,
    "score": 0,
    "user_id": 1,
    "completed": False
},{
    "id": 3,
    "assignment_name": "assignment_name",
    "module_name": "module_name",
    "deadline": datetime.date.today().strftime("%Y-%m-%d") + datetime.timedelta(days=2).strftime("%Y-%m-%d"),
    "difficulty": 1,
    "score": 0,
    "user_id": 1,
    "completed": False
}]
"""

def test_add_assignment(monkeypatch):
    # Simulate user input for assignment details
    inputs = iter([
        "Test Assignment",  # Assignment name
        "Test Module",      # Module name
        "2024-12-31",       # Deadline
        "3"                 # Difficulty level
    ])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Call the function to add an assignment
    result = add_assignment([])

    # Check if the function returns the expected status code
    assert result == 200
    assert Assignments.find("assignments", {"assignment_name": "Test Assignment101"}) is not None

def test_add_assignment_invalid_difficulty(monkeypatch):
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
    result = add_assignment([])

    # Check if the function returns the expected status code
    assert result == 200
    assert Assignments.find("assignments", {"assignment_name": "Test Assignment102"}) is not None

def test_add_assignment_empty_fields(monkeypatch):
    # Simulate user input for assignment details with empty fields
    inputs = iter([
        "",                 # Empty assignment name
        "Test Assignment",  # Valid assignment name
        "",                 # Empty module name
        "Test Module",      # Valid module name
        "",                 # Empty deadline
        "2024-12-31",       # Valid deadline
        "",                 # Empty difficulty level
        "3"                 # Valid difficulty level
    ])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Call the function to add an assignment
    result = add_assignment([])

    # Check if the function returns the expected status code
    assert result == 200
    assert Assignments.find("assignments", {"assignment_name": "Test Assignment103"}) is not None
def test_add_assignment_invalid_deadline(monkeypatch):
    # Simulate user input for assignment details with invalid deadline format
    inputs = iter([
        "Test Assignment",  # Assignment name
        "Test Module",      # Module name
        "31-12-2024",       # Invalid deadline format
        "2024-12-31",       # Valid deadline format
        "3"                 # Difficulty level
    ])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Call the function to add an assignment
    result = add_assignment([])

    # Check if the function returns the expected status code
    assert result == 200
    assert Assignments.find("assignments", {"assignment_name": "Test Assignment104"}) is not None
    
def test_add_assignment_invalid_deadline_format(monkeypatch):
    # Simulate user input for assignment details with invalid deadline format
    inputs = iter([
        "Test Assignment",  # Assignment name
        "Test Module",      # Module name
        "2024/12/31",       # Invalid deadline format
        "2024-12-31",       # Valid deadline format
        "3"                 # Difficulty level
    ])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Call the function to add an assignment
    result = add_assignment([])

    # Check if the function returns the expected status code
    assert result == 200
    assert Assignments.find("assignments", {"assignment_name": "Test Assignment105"}) is not None

def test_add_assignment_invalid_deadline_format2(monkeypatch):
    # Simulate user input for assignment details with invalid deadline format
    inputs = iter([
        "Test Assignment",  # Assignment name
        "Test Module",      # Module name
        "2024-31-12",       # Invalid deadline format
        "2024-12-31",       # Valid deadline format
        "3"                 # Difficulty level
    ])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Call the function to add an assignment
    result = add_assignment([])

    # Check if the function returns the expected status code
    assert result == 200
    assert Assignments.find("assignments", {"assignment_name": "Test Assignment106"}) is not None
