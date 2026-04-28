
s1_name = "Sangeet"
s1_mark = 85
s1_attendance = 90

s2_name = "Aman"
s2_mark = 90
s2_attendance = 88

def calculate_grade(marks) :
    if marks >= 90 :
        return "A"
    elif marks >= 75 :
       return "B"
    else :
        return "C"
        
def update_marks(old_marks , new_marks) :
    return new_marks

print("Student : ", s1_name)
print("Mark : ", s1_mark)
print("Grade : ", calculate_grade(s1_mark))
print("Attendance: ",s1_attendance)
# print(update_marks)
print()


print("Student: ",s2_name)
print("Marks: ",s2_mark)
print("Attendance: ",s2_attendance)
print("Grade: ",calculate_grade(s2_mark))
print()

s1_mark = update_marks(s1_mark,95)
print("Ater update")
print("Student : ", s1_name)
print("Mark : ", s1_mark)
print("Grade : ", calculate_grade(s1_mark))

print()
