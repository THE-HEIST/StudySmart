import pytest
from src.core.common.calculate_priority import calculate_priority, calculate_priority_score
from datetime import datetime

assignment = [{
    "id": 1,
    "assignment_name": "assignment_name",
    "module_name": "module_name",
    "deadline": datetime.date.today().strftime("%Y-%m-%d") + datetime.timedelta(days=2).strftime("%Y-%m-%d"),
    "difficulty": 4,
    "score": 0,
    "user_id": 1,
    "completed": True
},{
    "id": 2,
    "assignment_name": "assignment_name",
    "module_name": "module_name",
    "deadline": datetime.date.today().strftime("%Y-%m-%d") + datetime.timedelta(days=2).strftime("%Y-%m-%d"),
    "difficulty": 2,
    "score": 0,
    "user_id": 1,
    "completed": False
}]

def test_calculate_priority():
    assert calculate_priority_score(assignment[1]) == 1
    assert calculate_priority_score(assignment[0]) == 2

def test_calculate_priority_negative():
    with pytest.raises(ValueError):
        calculate_priority_score(-1)