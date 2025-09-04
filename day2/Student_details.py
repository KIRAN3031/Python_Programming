s_number, s_name = map(str, input("Enter roll number and name: ").split())
marks_input = input("Enter marks in three subjects: ").split()
s_m1, s_m2, s_m3 = map(int, marks_input)

print("Student name:", s_name)
print("Student roll number:", s_number)
print("Student marks in three subjects:", s_m1, s_m2, s_m3)

total = s_m1 + s_m2 + s_m3
print("Student total marks:", total)

average = round(total / 3, 2)
print("Student average marks:", average)

if s_m1 >= 40 and s_m2 >= 40 and s_m3 >= 40:
    print(f"The student with the student id {s_number} is passed")
    if average < 50:
        print("The Student Grade is C")
    elif 50 <= average < 70:
        print("The Student Grade is B")
    elif 70 <= average < 80:
        print("The Student Grade is A")
    else:
        print("The Student Grade is A+")
else:
    print(f"The student with the student id {s_number} failed the exam")
