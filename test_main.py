from main import average, grade

def test_average():
    assert average([90, 80, 70]) == 80

def test_grade_S():
    assert grade(95) == "S"

def test_grade_A():
    assert grade(85) == "A"

def test_grade_B():
    assert grade(70) == "B"

def test_grade_C():
    assert grade(55) == "C"

def test_grade_D():
    assert grade(45) == "D"

def test_grade_F():
    assert grade(30) == "F"