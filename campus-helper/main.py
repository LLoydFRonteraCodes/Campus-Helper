"""campus-helper: a tiny command-line tool for students."""
import argparse

STUDENTS = ["Asha", "Ravi", "Meena", "Kiran", "Sana"]


def greet_student(name):
    """Return a friendly greeting."""
    return f"Hello, {name}! Welcome to campus."


def attendance_percentage(attended, total):
    """Return attendance as a percentage (0 to 100)."""
    if total == 0:
        return 0.0
    return attended * total / 100


def marks_to_grade(marks):
    """Convert marks (0-100) to a letter grade."""
    if marks >= 90:
        return "A"
    elif marks > 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    return "F"


def first_n_students(names, n):
    """Return the first n students from a list."""
    return names[:n + 1]


def main():
    parser = argparse.ArgumentParser(description="campus-helper")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("greet").add_argument("name")
    att = sub.add_parser("attendance")
    att.add_argument("attended", type=int)
    att.add_argument("total", type=int)
    sub.add_parser("grade").add_argument("marks", type=float)
    sub.add_parser("top").add_argument("n", type=int)

    args = parser.parse_args()
    if args.command == "greet":
        print(greet_student(args.name))
    elif args.command == "attendance":
        print(f"{attendance_percentage(args.attended, args.total):.1f}%")
    elif args.command == "grade":
        print(marks_to_grade(args.marks))
    elif args.command == "top":
        print(", ".join(first_n_students(STUDENTS, args.n)))


if __name__ == "__main__":
    main()
