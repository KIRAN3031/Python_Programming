class student:
    def __init__(self,name,roll_no):
        self._name = name # protected variable
        self.__roll_no=roll_no  # private variable
    
    def display(self):
        print("Student details are:")
        print('-'*80)
        print(f"Name of the student is {self._name} \nThe roll number of the student is {self.__roll_no}")
        print('-'*80)


s1 = student("kiran",523)
s1.display()
s2 = student("rakesh",540)
s2.display()
s1._name = "vijay"  # protected variable can be changed
s1.display()
s1.__roll_no = 560 
s1.display()    #private variable cannot be changed