
# Function to calculate average
def average(marks):
    return sum(marks) / len(marks)


# Function to calculate grade
def grade(avg):
    if avg >= 90:
        return "S"
    elif avg >= 80:
        return "A"
    elif avg >= 65:
        return "B"
    elif avg >= 50:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"


# Function to display remarks
def remark(avg):
    if avg >= 90:
        return "Outstanding!"
    elif avg >= 80:
        return "Excellent!"
    elif avg >= 65:
        return "Very Good!"
    elif avg >= 50:
        return "Good!"
    elif avg >= 40:
        return "Needs Improvement!"
    else:
        return "Failed!"


# Main program
if __name__ == "__main__":

    print("STUDENT GRADE CALCULATOR")

    name = input("Enter student name: ")
    department = input("Enter department: ")
    semester = int(input("Enter semester: "))

    marks = []

    for i in range(3):
        mark = int(input("Enter marks for subject " + str(i + 1) + ": "))
        marks.append(mark)

    avg = average(marks)

    print("\n--- STUDENT RESULT ---")
    print("Name:", name)
    print("Department:", department)
    print("Semester:", semester)
    print("Marks:", marks)
    print("Average:", avg)
    print("Grade:", grade(avg))
    print("Remark:", remark(avg))
