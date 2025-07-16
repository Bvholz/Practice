exam1_grade = float(input("Enter score on Exam 1 (out of 100): "))
exam2_grade = float(input("Enter score on Exam 2 (out of 100): "))
exam3_grade = float(input("Enter score on Exam 3 (out of 100): "))

overall_grade = (exam1_grade + exam2_grade + exam3_grade) / 3

print(f"Your overall grade is: {overall_grade}")