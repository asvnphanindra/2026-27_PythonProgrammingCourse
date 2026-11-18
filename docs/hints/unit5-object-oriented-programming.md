# Unit V: Object-Oriented Programming — Hints

Use these hints to plan each program (input, process, output) and to check your results with the sample values.

Back to [Hints index](README.md) · [Lab tasks for this unit](../lab-tasks/unit5-object-oriented-programming.md)

Jump to a task:

**Unit 5A:** [Task 1](#unit-5a-task-1) · [Task 2](#unit-5a-task-2) · [Task 3](#unit-5a-task-3) · [Task 4](#unit-5a-task-4) · [Task 5](#unit-5a-task-5)

**Unit 5B:** [Task 1](#unit-5b-task-1) · [Task 2](#unit-5b-task-2) · [Task 3](#unit-5b-task-3) · [Task 4](#unit-5b-task-4) · [Task 5](#unit-5b-task-5)

**Unit 5C:** [Task 1](#unit-5c-task-1) · [Task 2](#unit-5c-task-2) · [Task 3](#unit-5c-task-3)

**Unit 5D:** [Task 1](#unit-5d-task-1)

---

<a id="unit-5a-task-1"></a>

## Unit 5A Task 1: Class and object

Creates a class, makes an object, and accesses attributes and methods.

### Analyse the problem: Identify Input, Process and Output

**Input**
- Values to store in object attributes (for example name and age)

**Process**
- Define a class with attributes and at least one method
- Create an object: `obj = ClassName()`
- Access with `obj.attribute` and `obj.method()`

**Output**
- Printed attribute values and method results

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
class ____:  # e.g. Student
    def greet(self):
        print("Hello from", self.____)

student = ____()  # create object
student.name = ____  # e.g. "Anu"
student.age = ____  # e.g. 20
print(student.____, student.____)
student.____()
```

### Example

| Item | Details |
|------|---------|
| **Example input** | name `Anu`, age `20` |
| **Example output** | `Anu 20`<br>`Hello from Anu` |

<a href="../../.faculty/solutions/h4o8px.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit5-object-oriented-programming.md).

---

<a id="unit-5a-task-2"></a>

## Unit 5A Task 2: Constructor (`__init__`)

Initializes object attributes when the object is created.

### Analyse the problem: Identify Input, Process and Output

**Input**
- Values passed when creating the object

**Process**
- Define `__init__(self, ...)`
- Assign `self.attr = value`
- Create objects with arguments: `ClassName(arg1, arg2)`

**Output**
- Object details printed after construction

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
class Student:
    def ____(self, name, age):  # __init__
        self.name = ____
        self.age = ____

    def display(self):
        print(self.name, self.age)

s1 = Student(____, ____)  # e.g. "Ravi", 21
s1.____()
```

### Example

| Item | Details |
|------|---------|
| **Example input** | `Student("Ravi", 21)` |
| **Example output** | `Ravi 21` |

<a href="../../.faculty/solutions/i5p9qy.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit5-object-oriented-programming.md).

---

<a id="unit-5a-task-3"></a>

## Unit 5A Task 3: Instance, class and static methods

Shows the three common method types in one class.

### Analyse the problem: Identify Input, Process and Output

**Input**
- Sample data for an instance and a class-level value

**Process**
- Instance method: first parameter `self`
- Class method: `@classmethod` and `cls`
- Static method: `@staticmethod` (no `self` / `cls` required)

**Output**
- Results from calling each kind of method

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
class Demo:
    college = ____  # e.g. "RVRJC"

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
Demo.____()
```

### Example

| Item | Details |
|------|---------|
| **Example output** | `Instance: Anu`<br>`Class: RVRJC`<br>`Static: utility message` |

<a href="../../.faculty/solutions/j6q0rz.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit5-object-oriented-programming.md).

---

<a id="unit-5a-task-4"></a>

## Unit 5A Task 4: Encapsulation (private and protected)

Uses naming conventions for protected (`_`) and private (`__`) attributes.

### Analyse the problem: Identify Input, Process and Output

**Input**
- Values for public, protected, and private fields

**Process**
- Protected: `_attr` (convention: for subclass / internal use)
- Private: `__attr` (name-mangled to `_Class__attr`)
- Access private data through a public method inside the class

**Output**
- Show what can be accessed directly vs through methods

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._branch = ____  # protected, e.g. "Main"
        self.____ = balance  # private, e.g. __balance

    def get_balance(self):
        return self.____

acc = BankAccount("Sita", 1000)
print(acc.owner, acc.____)
print("Balance:", acc.____())
# print(acc.__balance)  # would fail from outside
```

### Example

| Item | Details |
|------|---------|
| **Example input** | owner `Sita`, balance `1000` |
| **Example output** | `Sita Main`<br>`Balance: 1000` |

<a href="../../.faculty/solutions/k7r1sa.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit5-object-oriented-programming.md).

---

<a id="unit-5a-task-5"></a>

## Unit 5A Task 5: Getter and setter methods

Controls access to an attribute with get/set methods (or `@property`).

### Analyse the problem: Identify Input, Process and Output

**Input**
- A value to set (valid and invalid cases help show validation)

**Process**
- Store a private attribute
- Provide `get_...` / `set_...` (or `@property` / `@x.setter`)
- Optionally reject invalid values in the setter

**Output**
- Current value after get/set; error message if invalid

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
class Student:
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
s.set_marks(____)  # e.g. 150 → invalid
```

### Example

| Item | Details |
|------|---------|
| **Example input** | set `85`, then set `150` |
| **Example output** | `Marks: 85`<br>`Invalid marks` |

<a href="../../.faculty/solutions/l8s2tb.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit5-object-oriented-programming.md).

---

<a id="unit-5b-task-1"></a>

## Unit 5B Task 1: Single inheritance

A child class inherits from one parent class.

### Analyse the problem: Identify Input, Process and Output

**Input**
- Values used by parent and child attributes/methods

**Process**
- Define parent class
- Define `class Child(Parent):`
- Create a child object and call inherited and own methods

**Output**
- Messages showing parent behaviour reused by the child

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
class Person:
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
s.____()
```

### Example

| Item | Details |
|------|---------|
| **Example input** | name `Anu`, course `Python` |
| **Example output** | `Name: Anu`<br>`Course: Python` |

<a href="../../.faculty/solutions/m9t3uc.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit5-object-oriented-programming.md).

---

<a id="unit-5b-task-2"></a>

## Unit 5B Task 2: Multiple and multilevel inheritance

Demonstrates both multiple inheritance and a multilevel chain.

### Analyse the problem: Identify Input, Process and Output

**Input**
- Simple class hierarchies (no user input required)

**Process**
- Multilevel: `A → B → C` (grandchild uses both levels)
- Multiple: `class C(A, B):` combines two parents
- Call methods from each parent through the child

**Output**
- Prints that show which parent methods are available

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
# Multilevel
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
ch.____(); ch.____()
```

### Example

| Item | Details |
|------|---------|
| **Example output** | `Feature A` / `Feature B` / `Feature C`<br>`Father skill` / `Mother skill` |

<a href="../../.faculty/solutions/n0u4vd.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit5-object-oriented-programming.md).

---

<a id="unit-5b-task-3"></a>

## Unit 5B Task 3: Method overriding

Child class redefines a method that already exists in the parent.

### Analyse the problem: Identify Input, Process and Output

**Input**
- Optional values for parent/child objects

**Process**
- Parent defines a method (for example `display`)
- Child defines the same method name with new behaviour
- Optionally call parent version with `super().method()`

**Output**
- Child’s overridden message (and parent’s if you call `super`)

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
class Animal:
    def sound(self):
        print(____)  # e.g. "Some sound"

class Dog(Animal):
    def sound(self):
        print(____)  # e.g. "Bark"

a = Animal()
d = Dog()
a.____()
d.____()  # overridden
```

### Example

| Item | Details |
|------|---------|
| **Example output** | `Some sound`<br>`Bark` |

<a href="../../.faculty/solutions/o1v5we.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit5-object-oriented-programming.md).

---

<a id="unit-5b-task-4"></a>

## Unit 5B Task 4: Polymorphism with method overriding

Same method name, different behaviour depending on the object type.

### Analyse the problem: Identify Input, Process and Output

**Input**
- A list (or loop) of related objects

**Process**
- Several subclasses override the same method
- Call that method in a loop without checking the exact type

**Output**
- Different messages from each subclass

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
class Shape:
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
    s.____()
```

### Example

| Item | Details |
|------|---------|
| **Example input** | square side `4`, circle radius `3` |
| **Example output** | `Square: 16`<br>`Circle: 28.26` |

<a href="../../.faculty/solutions/p2w6xf.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit5-object-oriented-programming.md).

---

<a id="unit-5b-task-5"></a>

## Unit 5B Task 5: Operator overloading

Defines how operators like `+` work for your class objects.

### Analyse the problem: Identify Input, Process and Output

**Input**
- Two objects of your class

**Process**
- Implement a special method such as `__add__`, `__str__`, or `__lt__`
- Use the operator between objects (`obj1 + obj2`)

**Output**
- Result of the overloaded operation

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def ____(self, other):  # __add__
        return Point(self.x + other.x, self.y + other.y)

    def ____(self):  # __str__
        return f"({self.x}, {self.y})"

p1 = Point(____, ____)
p2 = Point(____, ____)
print(p1 + p2)
```

### Example

| Item | Details |
|------|---------|
| **Example input** | `Point(1, 2)` + `Point(3, 4)` |
| **Example output** | `(4, 6)` |

<a href="../../.faculty/solutions/q3x7yg.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit5-object-oriented-programming.md).

---

<a id="unit-5c-task-1"></a>

## Unit 5C Task 1: Abstraction with ABC

Uses `abc.ABC` and `@abstractmethod` so subclasses must implement required methods.

### Analyse the problem: Identify Input, Process and Output

**Input**
- Values for concrete subclasses (for example shapes)

**Process**
- Import `ABC`, `abstractmethod` from `abc`
- Define an abstract class with at least one `@abstractmethod`
- Implement the method in subclasses; do not instantiate the abstract class directly

**Output**
- Results from concrete subclass methods

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
from abc import ABC, ____

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
print("Area:", r.____())
```

### Example

| Item | Details |
|------|---------|
| **Example input** | rectangle `5` × `3` |
| **Example output** | `Area: 15` |

<a href="../../.faculty/solutions/r4y8zh.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit5-object-oriented-programming.md).

---

<a id="unit-5c-task-2"></a>

## Unit 5C Task 2: User-defined module

Creates a `.py` module and imports it from another program.

### Analyse the problem: Identify Input, Process and Output

**Input**
- Values passed into functions/classes defined in your module

**Process**
- Write helper code in a module file (for example `math_utils.py`)
- In the main file, `import math_utils` or `from math_utils import ...`
- Call the imported function/class

**Output**
- Result printed from the main driver program

### Sample input and output messages

**Program structure** (fill in the blanks):

```python
# math_utils.py
def add(a, b):
    return ____

# Unit-5C_Task-2_User_Defined_Module.py
import ____  # math_utils
print("Sum:", math_utils.____(10, 5))
```

> **Hint:** Keep the module file in the same folder as the main program (or on `PYTHONPATH`). Commit both files.

### Example

| Item | Details |
|------|---------|
| **Example input** | `add(10, 5)` |
| **Example output** | `Sum: 15` |

<a href="../../.faculty/solutions/s5z9ai.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit5-object-oriented-programming.md).

---

<a id="unit-5c-task-3"></a>

## Unit 5C Task 3: Custom package with multiple modules

Builds a package folder with `__init__.py` and more than one module, then imports from it.

### Analyse the problem: Identify Input, Process and Output

**Input**
- Values used by functions in different package modules

**Process**
- Create a package folder (for example `mypackage/`)
- Add `__init__.py` and at least two modules (for example `greetings.py`, `calc.py`)
- Import with `from mypackage.calc import add` (or similar)

**Output**
- Results from calling functions in different modules

### Sample input and output messages

**Program structure** (fill in the blanks):

```text
mypackage/
  __init__.py
  greetings.py   # def hello(name): ...
  calc.py        # def add(a, b): ...
```

```python
# Unit-5C_Task-3_Custom_Package.py
from mypackage.____ import hello
from mypackage.____ import add

print(hello(____))
print("Sum:", add(____, ____))
```

### Example

| Item | Details |
|------|---------|
| **Example input** | `hello("Anu")`, `add(2, 3)` |
| **Example output** | `Hello, Anu`<br>`Sum: 5` |

<a href="../../.faculty/solutions/t6a0bj.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit5-object-oriented-programming.md).

---

<a id="unit-5d-task-1"></a>

## Unit 5D Task 1: Mini application using OOP

Builds a small system (Library or Bank Account) using classes, objects, and methods.

### Analyse the problem: Identify Input, Process and Output

**Input**
- Menu choices and data (for example account deposit amount, or book title)

**Process**
- Design 1–3 classes with clear responsibilities
- Use encapsulation and methods for operations (deposit/withdraw, issue/return, etc.)
- Provide a simple menu loop or a short scripted demo of the main operations

**Output**
- Status messages after each operation (balance, issued books, etc.)

### Sample input and output messages

**Program structure** (fill in the blanks — Bank example):

```python
class BankAccount:
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
```

> **Hint:** Pick **one** theme (Library **or** Bank). Keep the demo short but show create + at least two operations + display status.

### Example

| Item | Details |
|------|---------|
| **Example (Bank)** | create account → deposit `500` → withdraw `200` → show balance `...` |
| **Example (Library)** | add book → issue book → return book → list available books |

<a href="../../.faculty/solutions/u7b1ck.md" target="_blank" rel="noopener noreferrer">View solution</a> (try the task first)

Back to [Lab tasks](../lab-tasks/unit5-object-oriented-programming.md).
