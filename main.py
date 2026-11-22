
<<<<<<< HEAD
# Function to calculate average marks
def average(marks):
    return sum(marks) / len(marks)


# Function to calculate grade
=======
import sys

# Calculate average
def average(marks):
    return sum(marks) / len(marks)

# Calculate grade
>>>>>>> 1292a3c38d104891db1cb4aeea2b5e118d80f3aa
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

<<<<<<< HEAD

# Function to check pass or fail
=======
# Check pass or fail
>>>>>>> 1292a3c38d104891db1cb4aeea2b5e118d80f3aa
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


# Function to display remarks
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
<<<<<<< HEAD

    print("STUDENT GRADE CALCULATOR")

    name = input("Enter student name: ")
    marks = []

    for i in range(3):
        mark = int(input("Enter marks for subject " + str(i + 1) + ": "))
        marks.append(mark)

    avg = average(marks)
    student_grade = grade(avg)

    print("\n----- STUDENT RESULT -----")
    print("Student Name:", name)
    print("Marks:", marks)
    print("Average Marks:", avg)
    print("Grade:", student_grade)
    print("Remark:", remark(avg))

    if is_pass(marks):
        print("Result: PASS")
    else:
        print("Result: FAIL")
=======
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
>>>>>>> 1292a3c38d104891db1cb4aeea2b5e118d80f3aa
