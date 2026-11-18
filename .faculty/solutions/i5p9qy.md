# Unit 5A Task 2 — Example solution

Demonstrate constructor (`__init__`) in a class.

```python
# Example solution: constructor __init__
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)


s1 = Student("Ravi", 21)
s1.display()
```

[Back to hint](../../docs/hints.md#unit-5a-task-2) · [Back to lab tasks](../../docs/lab-tasks/unit5-object-oriented-programming.md)
