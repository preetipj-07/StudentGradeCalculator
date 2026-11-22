# Function to calculate average marks
def average(marks):
    return sum(marks) / len(marks)

# Function to calculate grade
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

# Function to check pass or fail
def is_pass(marks):
    for mark in marks:
        if mark < 35:
            return False
    return True

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
print("STUDENT GRADE CALCULATOR")

name = input("Enter student name: ")

marks = []

for i in range(3):
    mark = int(input("Enter marks for subject " + str(i + 1) + ": "))
    marks.append(mark)

avg = average(marks)
student_grade = grade(avg)
print("Remark:", remark(avg))

print("\n----- STUDENT RESULT -----")
print("Student Name:", name)
print("Marks:", marks)
print("Average Marks:", avg)
print("Grade:", student_grade)

if is_pass(marks):
    print("Result: PASS")
else:
    print("Result: FAIL")
