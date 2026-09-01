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

def test_add_assignment_empty_fields(monkeypatch):
    Assignments.clear_all("assignments")
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
    result = add_assignment(Assignments=Assignments)

    # Check if the function returns the expected status code
    assert result == False
    #assert Assignments.find("assignments", "assignment_name", "Test Assignment") is not None

def test_add_assignment_invalid_deadline(monkeypatch):
    Assignments.clear_all("assignments")
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
    result = add_assignment(Assignments=Assignments)

    # Check if the function returns the expected status code
    assert result == False
    #assert Assignments.find("assignments", "assignment_name", "Test Assignment104") is not None

def test_add_assignment_invalid_deadline_format(monkeypatch):
    Assignments.clear_all("assignments")
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
    result = add_assignment(Assignments=Assignments)

    # Check if the function returns the expected status code
    assert result == False
    #assert Assignments.find("assignments", "assignment_name", "Test Assignment105") is not None

def test_add_assignment_invalid_deadline_format2(monkeypatch):
    Assignments.clear_all("assignments")
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
    result = add_assignment(Assignments=Assignments)

    # Check if the function returns the expected status code
    assert result == False
    #assert Assignments.find("assignments", "assignment_name", "Test Assignment106") is not None
