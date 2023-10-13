student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermine": 99,
    "Draco": 74,
    "Neville": 62}
student_grades = {}
for char in student_scores:
    if student_scores.get(char) >= 91:
        student_grades[char] = "Outstanding"
    elif student_scores.get(char) >= 81:
        student_grades[char] = "Exceedc Expectations"
    elif student_scores.get(char) >= 71:
        student_grades[char] = "Accepted"
    elif student_scores.get(char) <= 70:
        student_grades[char] = "Fail"
    else:
        print("System: Error Line 19")
for char in student_grades:
    print(f"{char}:  {student_grades.get(char)}")