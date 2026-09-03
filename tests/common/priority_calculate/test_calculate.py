import pytest
from src.core.common.calculate_priority import calculate_priority_score
from datetime import datetime, timedelta

assignment = [{
    "id": 1,
    "assignment_name": "assignment_name",
    "module_name": "module_name",
    "deadline": str(datetime.now().date() + timedelta(days=2)),
    "difficulty": 4,
    "score": 0,
    "user_id": 1,
    "completed": True
},{
    "id": 2,
    "assignment_name": "assignment_name",
    "module_name": "module_name",
    "deadline": str(datetime.now().date() + timedelta(days=2)),
    "difficulty": 2,
    "score": 0,
    "user_id": 1,
    "completed": False
}]

def test_calculate_priority():
    assert calculate_priority_score(assignment[1]) == pytest.approx(2/3)
    assert calculate_priority_score(assignment[0]) == pytest.approx(4/3)
