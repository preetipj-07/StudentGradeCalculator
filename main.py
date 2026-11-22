
import sys

# Calculate average
def average(marks):
    return sum(marks) / len(marks)

# Calculate grade
def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 35:
        return "D"
    else:
        return "F"

# Check pass or fail
def is_pass(marks):
    return all(mark >= 35 for mark in marks)

# Display remark
def remark(avg):
    if avg >= 90:
        return "Excellent!"
    elif avg >= 75:
        return "Very Good!"
    elif avg >= 60:
        return "Good!"
    elif avg >= 35:
        return "Keep practicing!"
    else:
        return "Needs improvement!"

# Main program
if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python main.py Name Mark1 Mark2 Mark3")
        sys.exit(1)

    name = sys.argv[1]
    marks = [int(x) for x in sys.argv[2:5]]

    avg = average(marks)

    print("Student Name:", name)
    print("Marks:", marks)
    print("Average:", avg)
    print("Grade:", grade(avg))
    print("Result:", "PASS" if is_pass(marks) else "FAIL")
    print("Remark:", remark(avg))
