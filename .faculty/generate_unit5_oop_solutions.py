"""Generate Unit 5 OOP solution notebooks from existing faculty solutions."""
from pathlib import Path

import nbformat as nbf

OUT_DIR = Path(__file__).resolve().parent


def md(text: str):
    return nbf.v4.new_markdown_cell(text.strip() + "\n")


def code(text: str):
    return nbf.v4.new_code_cell(text.strip() + "\n")


def save(name: str, title: str, cells: list):
    nb = nbf.v4.new_notebook()
    nb["cells"] = [
        md(f"# {title}\n\nExample solutions for {title.split('—')[0].strip()} tasks.")
    ] + cells
    nb["metadata"] = {
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python", "pygments_lexer": "ipython3"},
    }
    path = OUT_DIR / name
    nbf.write(nb, path)
    print(f"Wrote {path.name}")


# --- Unit 5A ---
save(
    "Unit-5A_Classes_and_Objects_Solutions.ipynb",
    "Unit 5A — Classes and Objects (Solutions)",
    [
        md("**Task 1**\n\nCreate a class and object, and access attributes/methods.\n\n**File:** `Unit-5A_Task-1_Class_and_Object.py`"),
        code('''# Example solution: class and object
class Student:
    def greet(self):
        print("Hello from", self.name)


student = Student()
student.name = "Anu"
student.age = 20
print(student.name, student.age)
student.greet()'''),
        md("**Task 2**\n\nDemonstrate constructor (`__init__`) in a class.\n\n**File:** `Unit-5A_Task-2_Constructor_Init.py`"),
        code('''# Example solution: constructor __init__
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)


s1 = Student("Ravi", 21)
s1.display()'''),
        md("**Task 3**\n\nDemonstrate instance methods, class methods and static methods.\n\n**File:** `Unit-5A_Task-3_Instance_Class_Static_Methods.py`"),
        code('''# Example solution: instance, class, and static methods
class Demo:
    college = "NRIU"

    def set_name(self, name):
        self.name = name
        print("Instance:", self.name)

    @classmethod
    def show_college(cls):
        print("Class:", cls.college)

    @staticmethod
    def info():
        print("Static: utility message")


obj = Demo()
obj.set_name("Anu")
Demo.show_college()
Demo.info()'''),
        md("**Task 4**\n\nDemonstrate encapsulation using private and protected attributes.\n\n**File:** `Unit-5A_Task-4_Encapsulation_Private_Protected.py`"),
        code('''# Example solution: private and protected attributes
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._branch = "Main"  # protected (convention)
        self.__balance = balance  # private (name-mangled)

    def get_balance(self):
        return self.__balance


acc = BankAccount("Sita", 1000)
print(acc.owner, acc._branch)
print("Balance:", acc.get_balance())'''),
        md("**Task 5**\n\nDemonstrate getter and setter methods.\n\n**File:** `Unit-5A_Task-5_Getter_Setter_Methods.py`"),
        code('''# Example solution: getter and setter methods
class Student:
    def __init__(self):
        self.__marks = 0

    def get_marks(self):
        return self.__marks

    def set_marks(self, value):
        if 0 <= value <= 100:
            self.__marks = value
        else:
            print("Invalid marks")


s = Student()
s.set_marks(85)
print("Marks:", s.get_marks())
s.set_marks(150)'''),
    ],
)

# --- Unit 5B ---
save(
    "Unit-5B_Inheritance_and_Polymorphism_Solutions.ipynb",
    "Unit 5B — Inheritance and Polymorphism (Solutions)",
    [
        md("**Task 1**\n\nDemonstrate single inheritance.\n\n**File:** `Unit-5B_Task-1_Single_Inheritance.py`"),
        code('''# Example solution: single inheritance
class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Name:", self.name)


class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def show_course(self):
        print("Course:", self.course)


s = Student("Anu", "Python")
s.show()
s.show_course()'''),
        md("**Task 2**\n\nDemonstrate multiple and multilevel inheritance.\n\n**File:** `Unit-5B_Task-2_Multiple_Multilevel_Inheritance.py`"),
        code('''# Example solution: multilevel and multiple inheritance
# Multilevel: A -> B -> C
class A:
    def feature_a(self):
        print("Feature A")


class B(A):
    def feature_b(self):
        print("Feature B")


class C(B):
    def feature_c(self):
        print("Feature C")


# Multiple: Child inherits Father and Mother
class Father:
    def skill_f(self):
        print("Father skill")


class Mother:
    def skill_m(self):
        print("Mother skill")


class Child(Father, Mother):
    pass


obj = C()
obj.feature_a()
obj.feature_b()
obj.feature_c()

ch = Child()
ch.skill_f()
ch.skill_m()'''),
        md("**Task 3**\n\nDemonstrate method overriding using inheritance.\n\n**File:** `Unit-5B_Task-3_Method_Overriding.py`"),
        code('''# Example solution: method overriding
class Animal:
    def sound(self):
        print("Some sound")


class Dog(Animal):
    def sound(self):
        print("Bark")


a = Animal()
d = Dog()
a.sound()
d.sound()'''),
        md("**Task 4**\n\nDemonstrate polymorphism using method overriding.\n\n**File:** `Unit-5B_Task-4_Polymorphism_Method_Overriding.py`"),
        code('''# Example solution: polymorphism with method overriding
class Shape:
    def area(self):
        print("Undefined")


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        print("Square:", self.side * self.side)


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        print("Circle:", 3.14 * self.r * self.r)


shapes = [Square(4), Circle(3)]
for s in shapes:
    s.area()'''),
        md("**Task 5**\n\nDemonstrate operator overloading.\n\n**File:** `Unit-5B_Task-5_Operator_Overloading.py`"),
        code('''# Example solution: operator overloading
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"


p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1 + p2)'''),
    ],
)

# --- Unit 5C ---
save(
    "Unit-5C_Abstraction_Modules_Packages_Solutions.ipynb",
    "Unit 5C — Abstraction, Modules and Packages (Solutions)",
    [
        md("**Task 1**\n\nDemonstrate abstraction using abstract classes (`ABC` module).\n\n**File:** `Unit-5C_Task-1_Abstraction_ABC.py`"),
        code('''# Example solution: abstract class with ABC
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h


r = Rectangle(5, 3)
print("Area:", r.area())'''),
        md(
            "**Task 2**\n\nCreate and import a user-defined module.\n\n"
            "**Files:** `math_utils.py` and `Unit-5C_Task-2_User_Defined_Module.py`\n\n"
            "Create `math_utils.py` with the first cell, then run the main program in the second cell "
            "(both files must be in the same folder)."
        ),
        code('''# math_utils.py
def add(a, b):
    return a + b'''),
        code('''# Example solution: import user-defined module
# Unit-5C_Task-2_User_Defined_Module.py
import math_utils

print("Sum:", math_utils.add(10, 5))'''),
        md(
            "**Task 3**\n\nCreate a custom package with multiple modules.\n\n"
            "**Files:** `mypackage/` (`__init__.py`, `greetings.py`, `calc.py`) and "
            "`Unit-5C_Task-3_Custom_Package.py`\n\n"
            "Create the package files shown below, then run the main program."
        ),
        code('''# mypackage/greetings.py
def hello(name):
    return f"Hello, {name}"'''),
        code('''# mypackage/calc.py
def add(a, b):
    return a + b'''),
        code('''# mypackage/__init__.py
# (can be empty)'''),
        code('''# Example solution: custom package with multiple modules
# Unit-5C_Task-3_Custom_Package.py
from mypackage.greetings import hello
from mypackage.calc import add

print(hello("Anu"))
print("Sum:", add(2, 3))'''),
    ],
)

# --- Unit 5D ---
save(
    "Unit-5D_Mini_Application_Solutions.ipynb",
    "Unit 5D — Mini Application (Solutions)",
    [
        md(
            "**Task 1**\n\nMini application using OOP concepts (Bank Account Management).\n\n"
            "**File:** `Unit-5D_Task-1_Mini_Application_OOP.py`\n\n"
            "Students may instead implement a Library Management System with classes such as "
            "`Book` and `Library` (add / issue / return / list)."
        ),
        code('''# Example solution: simple bank account mini application
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdraw amount")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print("Withdrawn:", amount)

    def display(self):
        print(f"Owner: {self.owner}, Balance: {self.__balance}")


acc = BankAccount("Krishna", 1000)
acc.display()
acc.deposit(500)
acc.withdraw(200)
acc.display()'''),
    ],
)

print("Done.")
