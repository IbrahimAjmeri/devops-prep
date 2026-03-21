def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "F"

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(10, 3) == 7

def test_multiply():
    assert multiply(3, 4) == 12

def test_grade_A():
    assert get_grade(95) == "A"

def test_grade_F():
    assert get_grade(40) == "F"
    