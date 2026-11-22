
from main import average, grade, is_pass, remark

def test_average():
    assert average([80, 90, 70]) == 80

def test_grade_A():
    assert grade(95) == "A"

def test_grade_B():
    assert grade(80) == "B"

def test_pass():
    assert is_pass([80, 70, 90]) == True

def test_fail():
    assert is_pass([80, 20, 90]) == False

def test_remark():
    assert remark(95) == "Excellent!"

def test_remark_good():
    assert remark(65) == "Good!"

def test_remark_fail():
    assert remark(20) == "Needs improvement!"
