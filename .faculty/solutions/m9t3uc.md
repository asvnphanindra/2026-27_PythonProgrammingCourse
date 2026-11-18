# Unit 5B Task 1 — Example solution

Demonstrate single inheritance.

```python
# Example solution: single inheritance
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
s.show_course()
```

[Back to hint](../../docs/hints.md#unit-5b-task-1) · [Back to lab tasks](../../docs/lab-tasks/unit5-object-oriented-programming.md)
