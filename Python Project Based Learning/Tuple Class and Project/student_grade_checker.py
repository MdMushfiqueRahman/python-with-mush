# Student Grade Checker


# Student Information (Tuple)
student = ("Mush", 101, 85, 90, 78)

# Tuple Unpacking
student_name, student_id, python_marks, math_marks, english_marks = student

# Calculate Total Marks
total_marks = python_marks + math_marks + english_marks

# Calculate Average
avg = total_marks / 3

# Grade Calculation
if avg >= 90:
    grade = "A"

elif avg >= 80:
    grade = "B"

elif avg >= 70:
    grade = "C"

elif avg >= 60:
    grade = "D"

else:
    grade = "F"

# Pass or Fail
if python_marks < 40 or math_marks < 40 or english_marks < 40:
    status = "FAIL"
else:
    status = "PASS"

# Student Report
print(f'''
====================================
         STUDENT GRADE CHECKER
====================================

          STUDENT INFORMATION
------------------------------------
Student Name : {student_name}
Student ID   : {student_id}

             SUBJECT MARKS
------------------------------------
Python       : {python_marks}
Math         : {math_marks}
English      : {english_marks}

             GRADE REPORT
------------------------------------
Total Marks  : {total_marks} / 300
Average Marks: {avg:.2f}
Grade        : {grade}

             FINAL RESULT
------------------------------------
Status       : {status}

====================================
       END OF STUDENT REPORT
====================================
''')