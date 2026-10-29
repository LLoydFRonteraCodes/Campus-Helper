from main import (
    greet_student,
    attendance_percentage,
    marks_to_grade,
    first_n_students,
)


def test_greet_student():
    assert greet_student("Asha") == "Hello, Asha! Welcome to campus."


def test_attendance_zero_total():
    assert attendance_percentage(0, 0) == 0.0


def test_attendance_percentage():
    assert attendance_percentage(45, 60) == 75.0


def test_grade_a_and_f():
    assert marks_to_grade(95) == "A"
    assert marks_to_grade(30) == "F"


def test_grade_boundary_80_is_b():
    assert marks_to_grade(80) == "B"


def test_first_n_students():
    assert first_n_students(["A", "B", "C", "D"], 2) == ["A", "B"]
