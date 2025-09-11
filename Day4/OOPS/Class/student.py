class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    
    def display(self):
        print("Student details are:")
        print('-'*80)
        print(f"Name of the student is {self.name} \nThe roll number of the student is {self.roll_no} \nThe marks of the student is {self.marks}")
        print('-'*80)

name = input("Enter the name of the student: ")
roll_no = int(input("Enter the roll number of the student: "))
marks = float(input("Enter the marks of the student: "))
s1 = Student(name,roll_no,marks)
s1.display()
s2 = Student("Rakesh",540,40)
s2.display()