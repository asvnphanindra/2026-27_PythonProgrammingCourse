# Unit 5A Task 5 — Example solution

Demonstrate getter and setter methods.

```python
# Example solution: getter and setter methods
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
s.set_marks(150)
```

[Back to hint](../../docs/hints/unit5-object-oriented-programming.md#unit-5a-task-5) · [Back to lab tasks](../../docs/lab-tasks/unit5-object-oriented-programming.md)
