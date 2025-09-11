class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def display(self):
        print("\nEmployee details are: ")
        print('_'*80)
        print(f"\nThe name of the employee is {self.name} and the salary of the employee is {self.salary}")
        print('_'*80)
    

class manager(employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department = department
    
    def display(self):
        super().display()
        print(f"The department of the manager is {self.department}")


m1 = manager("kiran",50000,"IT")
m1.display()
print()
e1 = employee("rakesh",40000)
e1.display()