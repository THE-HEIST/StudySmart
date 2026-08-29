import pytest
from datetime import datetime, timedelta
from src.core.common.calculate_priority import calculate_priority, calculate_priority_score, get_priority_level, view_priority_ranking

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

x1 = calculate_priority_score(assignment[0])
x2 = calculate_priority_score(assignment[1])
x3 = calculate_priority_score(assignment[2])

def test_calculate_priority_level():
    assert get_priority_level(x1) == "High"
    assert get_priority_level(x2) == "Medium"
    assert get_priority_level(x3) == "Low"

def test_failed_calculate_priority():
    with pytest.raises(ValueError):
        calculate_priority_score(-1)