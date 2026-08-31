from src.core.create.assignments import add_assignment
from src.core.read.assignments import view_assignments, view_order_by_undone, view_order_by_done, view_order_all, show_study_summary
from datetime import datetime, timedelta
from src.data_processing_module.config4test import test_assignments_db as Assignments
import pytest


test_table = ["""
{{"ID":<5}} {{"Assignment Name":<20}} {{"Module":<15}} {{"Deadline":<12}} {{"Difficulty":<10}} {{"Score":<8}} {{"Completed":<10}}
{{"-" * 90}}
{{"1":<5}} {{"Assignment 1":<20}} {{"Module 1":<15}} {{"2024-12-31":<12}} {{"3":<10}} {{"5":<8}} {{"Not Done":<10}}
{{"2":<5}} {{"Assignment 3":<20}} {{"Module 1":<15}} {{"2024-11-30":<12}} {{"2":<10}} {{"1":<8}} {{"Not Done":<10}}
{{"3":<5}} {{"Assignment 2":<20}} {{"Module 2":<15}} {{"2024-12-31":<12}} {{"2":<10}} {{"2":<8}} {{"Not Done":<10}}
""","""
{{"ID":<5}} {{"Assignment Name":<20}} {{"Module":<15}} {{"Deadline":<12}} {{"Difficulty":<10}} {{"Score":<8}} {{"Completed":<10}}
{{"-" * 90}}
{{"1":<5}} {{"Assignment 1":<20}} {{"Module 1":<15}} {{"2024-12-31":<12}} {{"3":<10}} {{"5":<8}} {{"Done":<10}}
{{"2":<5}} {{"Assignment 3":<20}} {{"Module 1":<15}} {{"2024-11-30":<12}} {{"2":<10}} {{"1":<8}} {{"Done":<10}}
{{"3":<5}} {{"Assignment 2":<20}} {{"Module 2":<15}} {{"2024-12-31":<12}} {{"2":<10}} {{"2":<8}} {{"Done":<10}}
""","""'
{{"ID":<5}} {{"Assignment Name":<20}} {{"Module":<15}} {{"Deadline":<12}} {{"Difficulty":<10}} {{"Score":<8}} {{"Completed":<10}}
{{"-" * 90}}
{{"1":<5}} {{"Assignment 1":<20}} {{"Module 1":<15}} {{"2024-12-31":<12}} {{"3":<10}} {{"5":<8}} {{"Not Done":<10}}
{{"2":<5}} {{"Assignment 3":<20}} {{"Module 1":<15}} {{"2024-11-30":<12}} {{"2":<10}} {{"1":<8}} {{"Not Done":<10}}
{{"3":<5}} {{"Assignment 2":<20}} {{"Module 2":<15}} {{"2024-12-31":<12}} {{"2":<10}} {{"2":<8}} {{"Done":<10}}
"""]

def test_view_assignments_undone(capsys):
    Assignments.clear_all("assignments")

    assignments = [
        {
            "assignment_name": "Assignment 1",
            "module_name": "Module 1",
            "deadline": "2024-12-31",
            "difficulty": 3,
            "score": 5,
            "completed": False
        },
        {
            "assignment_name": "Assignment 2",
            "module_name": "Module 2",
            "deadline": "2024-11-30",
            "difficulty": 2,
            "score": 1,
            "completed": False
        },
        {
            "assignment_name": "Assignment 3",
            "module_name": "Module 1",
            "deadline": "2024-12-31",
            "difficulty": 2,
            "score": 2,
            "completed": False
        }
    ]

    for i in assignments:
        Assignments.add("assignments", i)
    
    view_assignments(assignments=view_order_by_undone(Assignments=Assignments), Assignments=Assignments)

    captured = capsys.readouterr()
    assert "Assignment 1" in captured.out
    assert "Assignment 2" in captured.out
    assert "Assignment 3" in captured.out

def test_view_assignments_done(capsys):
    Assignments.clear_all("assignments")

    assignments = [
        {
            "assignment_name": "Assignment 1",
            "module_name": "Module 1",
            "deadline": "2024-12-31",
            "difficulty": 3,
            "score": 5,
            "completed": True
        },
        {
            "assignment_name": "Assignment 2",
            "module_name": "Module 2",
            "deadline": "2024-11-30",
            "difficulty": 2,
            "score": 1,
            "completed": True
        },
        {
            "assignment_name": "Assignment 3",
            "module_name": "Module 1",
            "deadline": "2024-12-31",
            "difficulty": 2,
            "score": 2,
            "completed": True
        }
    ]

    for i in assignments:
        Assignments.add("assignments", i)
    
    view_assignments(Assignments=Assignments, assignments=view_order_by_done(Assignments=Assignments, sort_key="score", reverse=True))

    captured = capsys.readouterr()
    assert "Assignment 1" in captured.out
    assert "Assignment 2" in captured.out
    assert "Assignment 3" in captured.out

def test_view_assignments_all(capsys):
    Assignments.clear_all("assignments")

    assignments = [
        {
            "assignment_name": "Assignment 1",
            "module_name": "Module 1",
            "deadline": "2024-12-31",
            "difficulty": 3,
            "score": 5,
            "completed": False
        },
        {
            "assignment_name": "Assignment 2",
            "module_name": "Module 2",
            "deadline": "2024-11-30",
            "difficulty": 2,
            "score": 1,
            "completed": True
        },
        {
            "assignment_name": "Assignment 3",
            "module_name": "Module 1",
            "deadline": "2024-12-31",
            "difficulty": 2,
            "score": 2,
            "completed": False
        }
    ]

    for i in assignments:
        Assignments.add("assignments", i)
    
    view_assignments(Assignments=Assignments, assignments=view_order_all(Assignments=Assignments))

    captured = capsys.readouterr()
    assert "Assignment 1" in captured.out
    assert "Assignment 2" in captured.out
    assert "Assignment 3" in captured.out