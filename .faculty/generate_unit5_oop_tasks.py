"""Generate Unit 5 OOP task notebooks (fill-in-the-blank style)."""
from pathlib import Path

import nbformat as nbf

OUT_DIR = Path(__file__).resolve().parent


def md(text: str):
    return nbf.v4.new_markdown_cell(text.strip() + "\n")


def code(text: str):
    return nbf.v4.new_code_cell(text.strip() + "\n")


def empty_code():
    return nbf.v4.new_code_cell("")


def task_block(title: str, concept: str | None, hint_code: str):
    body = title.strip()
    if concept:
        body += "\n\n**Concept**\n\n" + concept.strip()
    return [
        md(body),
        md("**Hint — fill in the blanks**"),
        code(hint_code),
        md("**Your complete program**"),
        empty_code(),
    ]


def save(name: str, title: str, cells: list):
    nb = nbf.v4.new_notebook()
    nb["cells"] = [md(f"# {title}\n\nFill in the blanks in the hint cell, then write your complete program in the empty cell below it.")] + cells
    nb["metadata"] = {
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python", "pygments_lexer": "ipython3"},
    }
    path = OUT_DIR / name
    nbf.write(nb, path)
    print(f"Wrote {path.name}")


# --- Unit 5A ---
cells_a = []
cells_a += task_block(
    "**Task 1**\n\nWrite a Python program that creates a class and object, and accesses attributes/methods.\n\n**File:** `Unit-5A_Task-1_Class_and_Object.py`",
    "- Define a class with attributes and at least one method\n"
    "- Create an object: `obj = ClassName()`\n"
    "- Access with `obj.attribute` and `obj.method()`",
    '''class ____:  # e.g. Student
    def greet(self):
        print("Hello from", self.____)

student = ____()  # create object
student.name = ____  # e.g. "Anu"
student.age = ____  # e.g. 20
print(student.____, student.____)
student.____()''',
)
cells_a += task_block(
    "**Task 2**\n\nWrite a Python program that demonstrates a constructor (`__init__` method) in a class.\n\n**File:** `Unit-5A_Task-2_Constructor_Init.py`",
    "- Define `__init__(self, ...)` to set attributes when the object is created\n"
    "- Assign with `self.attr = value`\n"
    "- Create objects with arguments: `ClassName(arg1, arg2)`",
    '''class Student:
    def ____(self, name, age):  # __init__
        self.name = ____
        self.age = ____

    def display(self):
        print(self.name, self.age)

s1 = Student(____, ____)  # e.g. "Ravi", 21
s1.____()''',
)
cells_a += task_block(
    "**Task 3**\n\nWrite a Python program that demonstrates instance methods, class methods, and static methods.\n\n**File:** `Unit-5A_Task-3_Instance_Class_Static_Methods.py`",
    "- Instance method: first parameter `self`\n"
    "- Class method: `@classmethod` and `cls`\n"
    "- Static method: `@staticmethod` (no `self` / `cls` required)",
    '''class Demo:
    college = ____  # e.g. "NRIU"

    def ____(self, name):  # instance method
        self.name = name
        print("Instance:", self.name)

    @____
    def show_college(cls):
        print("Class:", cls.____)

    @____
    def info():
        print("Static: utility message")

obj = Demo()
obj.____("Anu")
Demo.____()
Demo.____()''',
)
cells_a += task_block(
    "**Task 4**\n\nWrite a Python program that demonstrates encapsulation using private and protected attributes.\n\n**File:** `Unit-5A_Task-4_Encapsulation_Private_Protected.py`",
    "- Protected: `_attr` (convention: for subclass / internal use)\n"
    "- Private: `__attr` (name-mangled to `_Class__attr`)\n"
    "- Access private data through a public method inside the class",
    '''class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._branch = ____  # protected, e.g. "Main"
        self.____ = balance  # private, e.g. __balance

    def get_balance(self):
        return self.____

acc = BankAccount("Sita", 1000)
print(acc.owner, acc.____)
print("Balance:", acc.____())
# print(acc.__balance)  # would fail from outside''',
)
cells_a += task_block(
    "**Task 5**\n\nWrite a Python program that demonstrates getter and setter methods.\n\n**File:** `Unit-5A_Task-5_Getter_Setter_Methods.py`",
    "- Store a private attribute\n"
    "- Provide `get_...` / `set_...` (or `@property` / `@x.setter`)\n"
    "- Optionally reject invalid values in the setter",
    '''class Student:
    def __init__(self):
        self.____ = 0  # __marks

    def get_marks(self):
        return self.____

    def set_marks(self, value):
        if 0 <= value <= ____:
            self.__marks = ____
        else:
            print("Invalid marks")

s = Student()
s.____(85)
print("Marks:", s.____())
s.set_marks(____)  # e.g. 150 → invalid''',
)
save("Unit-5A_Classes_and_Objects_Tasks.ipynb", "Unit 5A — Classes and Objects (Tasks)", cells_a)

# --- Unit 5B ---
cells_b = []
cells_b += task_block(
    "**Task 1**\n\nWrite a Python program that demonstrates single inheritance.\n\n**File:** `Unit-5B_Task-1_Single_Inheritance.py`",
    "- Define a parent class\n"
    "- Define `class Child(Parent):`\n"
    "- Create a child object and call inherited and own methods",
    '''class Person:
    def __init__(self, name):
        self.name = ____

    def show(self):
        print("Name:", self.name)

class Student(____):
    def __init__(self, name, course):
        ____.__init__(self, name)  # or super().__init__(name)
        self.course = ____

    def show_course(self):
        print("Course:", self.course)

s = Student(____, ____)  # e.g. "Anu", "Python"
s.____()
s.____()''',
)
cells_b += task_block(
    "**Task 2**\n\nWrite a Python program that demonstrates multiple and multilevel inheritance.\n\n**File:** `Unit-5B_Task-2_Multiple_Multilevel_Inheritance.py`",
    "- Multilevel: `A → B → C` (grandchild uses both levels)\n"
    "- Multiple: `class C(A, B):` combines two parents\n"
    "- Call methods from each parent through the child",
    '''# Multilevel
class A:
    def feature_a(self):
        print("Feature A")

class B(____):
    def feature_b(self):
        print("Feature B")

class C(____):
    def feature_c(self):
        print("Feature C")

# Multiple
class Father:
    def skill_f(self):
        print("Father skill")

class Mother:
    def skill_m(self):
        print("Mother skill")

class Child(____, ____):
    pass

obj = C()
obj.feature_a(); obj.feature_b(); obj.feature_c()
ch = Child()
ch.____(); ch.____()''',
)
cells_b += task_block(
    "**Task 3**\n\nWrite a Python program that demonstrates method overriding using inheritance.\n\n**File:** `Unit-5B_Task-3_Method_Overriding.py`",
    "- Parent defines a method (for example `sound`)\n"
    "- Child defines the same method name with new behaviour\n"
    "- Optionally call parent version with `super().method()`",
    '''class Animal:
    def sound(self):
        print(____)  # e.g. "Some sound"

class Dog(Animal):
    def sound(self):
        print(____)  # e.g. "Bark"

a = Animal()
d = Dog()
a.____()
d.____()  # overridden''',
)
cells_b += task_block(
    "**Task 4**\n\nWrite a Python program that demonstrates polymorphism using method overriding.\n\n**File:** `Unit-5B_Task-4_Polymorphism_Method_Overriding.py`",
    "- Several subclasses override the same method\n"
    "- Call that method in a loop without checking the exact type\n"
    "- Same method name, different behaviour depending on the object",
    '''class Shape:
    def area(self):
        print("Undefined")

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        print("Square:", self.side * ____)

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        print("Circle:", 3.14 * self.r * ____)

shapes = [Square(____), Circle(____)]  # e.g. 4, 3
for s in shapes:
    s.____()''',
)
cells_b += task_block(
    "**Task 5**\n\nWrite a Python program that demonstrates operator overloading.\n\n**File:** `Unit-5B_Task-5_Operator_Overloading.py`",
    "- Implement a special method such as `__add__`, `__str__`, or `__lt__`\n"
    "- Use the operator between objects (`obj1 + obj2`)\n"
    "- `__str__` controls how the object prints",
    '''class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def ____(self, other):  # __add__
        return Point(self.x + other.x, self.y + other.y)

    def ____(self):  # __str__
        return f"({self.x}, {self.y})"

p1 = Point(____, ____)
p2 = Point(____, ____)
print(p1 + p2)''',
)
save("Unit-5B_Inheritance_and_Polymorphism_Tasks.ipynb", "Unit 5B — Inheritance and Polymorphism (Tasks)", cells_b)

# --- Unit 5C ---
cells_c = []
cells_c += task_block(
    "**Task 1**\n\nWrite a Python program that demonstrates abstraction using abstract classes (`ABC` module).\n\n**File:** `Unit-5C_Task-1_Abstraction_ABC.py`",
    "- Import `ABC`, `abstractmethod` from `abc`\n"
    "- Define an abstract class with at least one `@abstractmethod`\n"
    "- Implement the method in subclasses; do not instantiate the abstract class directly",
    '''from abc import ABC, ____

class Shape(____):
    @____
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h
    def area(self):
        return self.w * ____

r = Rectangle(____, ____)  # e.g. 5, 3
print("Area:", r.____())''',
)
cells_c += task_block(
    "**Task 2**\n\nWrite a Python program that creates and imports a user-defined module.\n\n**File:** `Unit-5C_Task-2_User_Defined_Module.py` (plus a helper module such as `math_utils.py`)",
    "- Write helper code in a module file (for example `math_utils.py`)\n"
    "- In the main file, `import math_utils` or `from math_utils import ...`\n"
    "- Keep the module in the same folder as the main program and commit both files",
    '''# math_utils.py
def add(a, b):
    return ____

# Unit-5C_Task-2_User_Defined_Module.py
import ____  # math_utils
print("Sum:", math_utils.____(10, 5))''',
)
cells_c += task_block(
    "**Task 3**\n\nWrite a Python program that creates a custom package with multiple modules.\n\n**File:** `Unit-5C_Task-3_Custom_Package.py` (plus a package folder such as `mypackage/`)",
    "- Create a package folder (for example `mypackage/`)\n"
    "- Add `__init__.py` and at least two modules (for example `greetings.py`, `calc.py`)\n"
    "- Import with `from mypackage.calc import add` (or similar)",
    '''# Package layout (create these files):
# mypackage/
#   __init__.py
#   greetings.py   # def hello(name): ...
#   calc.py        # def add(a, b): ...

from mypackage.____ import hello
from mypackage.____ import add

print(hello(____))
print("Sum:", add(____, ____))''',
)
save("Unit-5C_Abstraction_Modules_Packages_Tasks.ipynb", "Unit 5C — Abstraction, Modules and Packages (Tasks)", cells_c)

# --- Unit 5D ---
cells_d = []
cells_d += task_block(
    "**Task 1**\n\nImplement a mini application using OOP concepts (for example Library Management System or Bank Account Management System).\n\n**File:** `Unit-5D_Task-1_Mini_Application_OOP.py`",
    "- Design 1–3 classes with clear responsibilities\n"
    "- Use encapsulation and methods for operations (deposit/withdraw, issue/return, etc.)\n"
    "- Provide a simple menu loop or a short scripted demo\n"
    "- Pick **one** theme (Library **or** Bank). Show create + at least two operations + display status",
    '''class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.____ = balance  # prefer private/protected balance

    def deposit(self, amount):
        ____
    def withdraw(self, amount):
        ____
    def display(self):
        ____

# create account, deposit, withdraw, display
# Example: create → deposit 500 → withdraw 200 → show balance''',
)
save("Unit-5D_Mini_Application_Tasks.ipynb", "Unit 5D — Mini Application (Tasks)", cells_d)

print("Done.")
