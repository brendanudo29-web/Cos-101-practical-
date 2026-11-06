student_name = input("Enter student name")
course_work = float(input("Enter coursework"))
if course_work > 30:
    print("invalid course_work")
else:
    Examination_score =float(input("Enter score"))
    if Examination_score  > 70:
        print("invalid score")
    elif Examination_score < 0 or Examination_score < 70:
       print(" Assign_grade")
        
