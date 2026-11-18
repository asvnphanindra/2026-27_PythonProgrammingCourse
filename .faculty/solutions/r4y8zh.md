# Unit 5C Task 1 — Example solution

Demonstrate abstraction using abstract classes (`ABC` module).

```python
# Example solution: abstract class with ABC
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
print("Area:", r.area())
```

[Back to hint](../../docs/hints/unit5-object-oriented-programming.md#unit-5c-task-1) · [Back to lab tasks](../../docs/lab-tasks/unit5-object-oriented-programming.md)
