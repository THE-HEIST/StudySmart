import pytest
from datetime import datetime, timedelta, timedelta
from src.core.common.calculate_priority import calculate_priority_score, get_priority_level

assignment = [{
    "id": 1,
    "assignment_name": "assignment_name",
    "module_name": "module_name",
    "deadline": str(datetime.now().date() + timedelta(days=1)),
    "difficulty": 4,
    "score": 0,
    "user_id": 1,
    "completed": True
},{
    "id": 2,
    "assignment_name": "assignment_name",
    "module_name": "module_name",
    "deadline": str(datetime.now().date() + timedelta(days=1)),
    "difficulty": 2,
    "score": 0,
    "user_id": 1,
    "completed": False
},{
    "id": 3,
    "assignment_name": "assignment_name",
    "module_name": "module_name",
    "deadline": str(datetime.now().date() + timedelta(days=2)),
    "difficulty": 1,
    "score": 0,
    "user_id": 1,
    "completed": False
}]

x1 = calculate_priority_score(assignment[0])
x2 = calculate_priority_score(assignment[1])
x3 = calculate_priority_score(assignment[2])

def test_calculate_priority_level():
    assert get_priority_level(x1) == "HIGH"
    assert get_priority_level(x2) == "MEDIUM"
    assert get_priority_level(x3) == "LOW"

"""
def test_failed_calculate_priority():
    with pytest.raises(ValueError):
        calculate_priority_score(-1)
"""