student_names = ("Juan", "Maria", "Joseph")
student_scores = (70, 90, 81)

for index, (student_name, student_score) in enumerate(zip(student_names, student_scores)):
    print(index, f"Student: {student_name} scored {student_score}")