students = (
    ("Mush", 101, 85, 90, 78),
    ("Rahim", 102, 92, 88, 95),
    ("Karim", 103, 67, 75, 80),
    ("Fardin", 104, 45, 35, 60),
    ("Sadia", 105, 38, 55, 42)
)

passed = 0
failed = 0
class_total = 0

highest_total = -1
lowest_total = 301

topper_name = ""
lowest_name = ""

python_highest = -1
math_highest = -1
english_highest = -1

python_topper = ""
math_topper = ""
english_topper = ""

print("""
=============================================
          STUDENT PERFORMANCE ANALYZER
=============================================

                STUDENT REPORT
---------------------------------------------
""")

for name, student_id, python_marks, math_marks, english_marks in students:

    total = python_marks + math_marks + english_marks
    average = total / 3

    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"

    if python_marks < 40 or math_marks < 40 or english_marks < 40:
        status = "FAIL"
        failed += 1
    else:
        status = "PASS"
        passed += 1

    if total > highest_total:
        highest_total = total
        topper_name = name

    if total < lowest_total:
        lowest_total = total
        lowest_name = name

    if python_marks > python_highest:
        python_highest = python_marks
        python_topper = name

    if math_marks > math_highest:
        math_highest = math_marks
        math_topper = name

    if english_marks > english_highest:
        english_highest = english_marks
        english_topper = name

    class_total += total

    print(f"Student Name : {name}")
    print(f"Student ID   : {student_id}")
    print(f"Python       : {python_marks}")
    print(f"Math         : {math_marks}")
    print(f"English      : {english_marks}")
    print(f"Total        : {total}/300")
    print(f"Average      : {average:.2f}")
    print(f"Grade        : {grade}")
    print(f"Status       : {status}")
    print("---------------------------------------------")

total_students = len(students)
class_average = class_total / (total_students * 3)

print(f"""
                  CLASS SUMMARY
---------------------------------------------
Total Students       : {total_students}
Passed Students      : {passed}
Failed Students      : {failed}

Class Average        : {class_average:.2f}

Class Topper          : {topper_name} ({highest_total}/300)
Lowest Performer     : {lowest_name} ({lowest_total}/300)

             SUBJECT-WISE TOPPERS
---------------------------------------------
Python Highest       : {python_topper} ({python_highest})
Math Highest         : {math_topper} ({math_highest})
English Highest      : {english_topper} ({english_highest})

=============================================
                 END OF REPORT
=============================================
""")