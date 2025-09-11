==================================================================================================
-------------------------------------------DAY 4--------------------------------------------------
==================================================================================================

# OOPS
    - Encapsulation
    - Inheritance
    - Abstraction
    - Polymorphism

# Object
    - An object is a instance of class ( An Object is a real world entity which is physically exisiting in the world)
    - An Object is a real world entity which has its own state and behaviour.
        ex : A person plays, thinks etc.

# Class
    - A class is a blue print of an object.
    - A class is group of objects

                                                                                        |----------------------------------------|
                                                                                        |           Obj Raju                     |                       
                                                                                        |----------------------------------------|
                                                                                        |   Name :  raju                         |
                                                                                        |   age :   20                           |~~~~ Variables
                                                                                        |   gen :    male                        |
                                                                                        |----------------------------------------|
                                                                                        |  work{}           talk{}               |
                                                                                        |    {}                 {}               |~~~~ Methods    --------------------------------|                                                                                                     
    |           Class Person                 |                       
    |----------------------------------------|
    |   Name :                               |
    |   age :                                |~~~~ Variables
    |   gen :                                |
    |----------------------------------------|
    |  work{}           talk{}               |
    |    {}                 {}               |~~~~ Methods    
    |----------------------------------------|                                                              

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# class defination
    class Employee:
    def __init__(self, name, age):
        self.name =  name
        self.age = age

# Object defination
    obj_name = class_name()


### problem
    - Task:
        Creae at least two student objects with different details.
        call the display() method for each object

        class Student:
            def __init__(self,name,roll_no,marks):
                self.name=name
                self.roll_no=name
                self.marks = marks

## Encapsulation
    - access modifiers
    - public (default)
    - private (__name) for the security
    - protected (_name) for using the inheritance

## Inheritance

    1.Single Inheritance
        A subclass inherits from one single parent class.
        Example: Class Car inherits from Class Vehicle.

                A
                |
                B

    2. Multilevel Inheritance
        A subclass inherits from a derived class, forming a chain of inheritance.
        Example: Class C inherits from B, and B inherits from A.

                A
                |
                B
                |
                C

    3. Multiple Inheritance
        A subclass inherits from more than one parent class, combining features from multiple base classes.
        Supported in Python, C++, but not in Java (which uses interfaces for similar purposes).

                A     B
                 \   /
                   C

    4. Hierarchical Inheritance
        Multiple subclasses inherit from a single parent class.
        Example: Classes B and C both inherit from Class A.

                  A
                /   \
                B   C

    5. Hybrid Inheritance
        A combination of two or more types of inheritance (e.g., multiple + multilevel) to form complex inheritance structures

                  A
                /   \
                B   C
                \   /
                  D

### problem
    Employee Manager problem using inheritance
    where employee class is the base class and the attributes are name and the salary and display() method that displays the details of the employeee
    and the class manager which is dervied form the class manager and has attribute departmnent and override the display method to it


# Abstraction 
    Abstraction is the concept of hiding complex implementation details and showing only the essential features of an object or system to the user. It helps manage complexity by exposing only what is necessary and hiding the inner workings.

    Abstract Class
    Definition:
        An abstract class is a class that cannot be instantiated directly. It acts as a blueprint for other classes, often containing one or more abstract methods (methods declared but not implemented) along with concrete methods (with implementation). It defines a common interface and structure that subclasses must follow.

    Key Points:
        Cannot create an object directly from an abstract class.

        Can contain both abstract methods (without body) and concrete methods.

        Can have constructors and member variables.

        Must be inherited by subclasses that provide implementation to the abstract methods.

        Helps enforce a contract for subclasses ensuring they implement required methods.

    Abstract Method
    Definition:
        An abstract method is a method that is declared without an implementation (no function body). Subclasses inheriting the abstract class must provide the implementation for all abstract methods.

### problem
    Create an abstract class Shape that defines:
    An abstract method area() (no implementation).
    Create two child classes that inherit from Shape:
    Rectangle → has attributes length, breadth, and implements area().
    Circle → has attribute radius, and implements area().
    Task:
    Define the abstract class Shape using the abc module.
    Implement Rectangle and Circle classes by providing their own version of area().
    Create one object of Rectangle and one of Circle, then display their areas.  
    from abc import ABC, abstractmethod 
    # Abstract class
    class Shape(ABC): 
        @abstractmethod           # Abstract method
        def area(self):
            pass   

 

# ploymorphism
    Definition:
        Polymorphism means "many forms" — it allows objects of different classes to be treated through the same interface, where each class can provide its own implementation of the shared methods

    Methods to Achieve Polymorphism:
        Method Overloading: Same method name with different parameters within the same class.

        Method Overriding: Subclass provides a specific implementation of a method defined in its superclass.

        Virtual Functions / Dynamic Dispatch: Used in languages like C++ and C# to enable runtime polymorphism.

        Interfaces & Abstract Classes: Define methods that must be implemented by derived classes, allowing runtime polymorphism.

### problem 
    You are asked to design a simple Payment System that can handle different payment methods
    Requirements:
    Create a base class Payment with a method pay(amount).
    Create three child classes that override the pay(amount) method:
    CashPayment → print "Paid ₹<amount> in cash"
    CardPayment → print "Paid ₹<amount> using credit/debit card"
    UPIPayment → print "Paid ₹<amount> using UPI"
    Task:
    Create a list of payment objects (CashPayment, CardPayment, UPIPayment).
    Loop through them and call pay(1000).
    Each object should print a different message.


### problem
    Create a class BankAccout with the following:
    A private variable __balance (default = 0)
    A method deposit(amount) -> adds money to balance
    A method withdraw(amount) -> deducts money if sufficient balance
    A method get_balance() -> returns the current balance

    Task:
    Create an object of BankAccount
    Deposit 50000
    withdraw 2000
    print()  final_balance

 
# Exception Handling

    when an errr occurs, or exception as we call it, Python will normally stop ad generate an error message.

    try
        this block lets you test a block of code for errors.

    except
        this block lets uou handle the error.

    else
        this block lets you execute code when there is no error.

    finally
        this block lets you execute code, regardless of the result of the try-and except blocks.

    Built-in Exceptions
        BaseException: The root class for all built-in exceptions. All other exceptions derive from this.
        Exception: The base class for most user-defined and built-in exceptions except system-exit related ones.
        ZeroDivisionError: Raised when dividing by zero.
        IndexError: Raised when trying to access an index that does not exist in a sequence.
        ValueError: Raised when a function receives an argument of the right type but inappropriate value.
        KeyError: Raised when a dictionary key is not found.
        TypeError: Raised when an operation or function is applied to an object of inappropriate type.
        FileNotFoundError: Raised when trying to open a file that does not exist.

### problem
    Zero Division Exception code

### project
    • Create classes Vehicle, ParkingSpot, and ParkingLot.
    • Create multiple objects (vehicles, spots, parking lot).
    • Demonstrate object creation, attribute initialization, and method calls.
    • Make sensitive attributes private (e.g., license plate, owner name, spot status).
    • Provide getter/setter methods to access/update them safely.
    • Show that direct access fails but methods work.
    • Vehicle is the base class.
    • Derived classes:
    Bike (extra attribute: helmet_required)
    Car (extra attribute: seats)
    SUV (extra attribute: four_wheel_drive)
    Truck (extra attribute: max_load_capacity)
    • Each child class overrides display() to print its own details.
    • Create a list of different vehicle objects (Bike, Car, SUV, Truck).
    • Iterate and call display() → each object responds differently.
    • Implement a calculate_parking_fee() method:
    Bike → ₹20/hour
    Car → ₹50/hour
    SUV → ₹70/hour
    Truck → ₹100/hour

    -----------------------------------------------------------------------------------------------

    • Demonstrate runtime polymorphism by calling the method on different objects.
    • Create an abstract class/interface Payment (using abc module).
    • Define an abstract method process_payment(amount).
    • Create child classes:
    CashPayment
    CardPayment
    UPIPayment
    • Demonstrate abstraction by processing payments differently (just print “Paid ₹X via UPI”).



    Task 1: Vehicle Classes
    Implement base and derived vehicle classes with encapsulation.
    Override display() and calculate_parking_fee().
    Task 2: ParkingSpot Class
    Implement ParkingSpot with size restrictions (S, M, L, XL).
    Methods: assign_vehicle(), remove_vehicle().
    Ensure vehicle type fits correct spot size (Bike → S+, Car → M+, SUV → L+, Truck → XL only).
    Task 3: ParkingLot Class
    Store multiple parking spots.
    Methods:
    add_spot() → add new parking spots.
    show_spots() → display all spots and their status.
    park_vehicle(vehicle) → find suitable spot and park.
    unpark_vehicle(vehicle) → remove from spot and calculate fee.
    Task 4: Payment (Abstraction + Polymorphism)
    When un-parking a vehicle, calculate fee (based on hours).
    Ask user for payment method → process payment using appropriate child class.
    Task 5: Main Program
    Create a parking lot with mixed spots.
    Create multiple vehicle objects.
    Park/unpark vehicles.
    Demonstrate encapsulation, inheritance, polymorphism, and abstraction throughout.