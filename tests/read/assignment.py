from src.core.create.assignments import add_assignment
from src.core.read.assignments import view_assignments, view_order_by_undone, view_order_by_done
from datetime import datetime
from src.data_processing_module.config4test import test_assignment_db as Assignments
import pytest

Assignments.clear_all("assignments")

test_table = [f"""
{{"ID":<5}} {{"Assignment Name":<20}} {{"Module":<15}} {{"Deadline":<12}} {{"Difficulty":<10}} {{"Score":<8}} {{"Completed":<10}}
{{"-" * 90}}
{{"1:<5}} {{"Assignment 1:<20}} {{"Module 1:<15}} {{"2024-12-31:<12}} {{"3:<10}} {{"0:<8}} {{"Not Done:<10}}
""",]

def test_view_assignments_und(capsys):
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
            "assignment_name": "Assignment 1",
            "module_name": "Module 1",
            "deadline": "2024-12-31",
            "difficulty": 2,
            "score": 2,
            "completed": False
        }
    ]

    for i in assignments:
        Assignments.add("assignments", i)
    
    x1 = view_assignments(view_order_by_undone())
    x2 = view_assignments(view_order_by_done())

    captured = capsys.readouterr()
    assert test_table[0] in captured.out
    assert "1. Assignment 1 - Not Completed" in captured.out
    assert "2. Assignment 2 - Completed" in captured.out