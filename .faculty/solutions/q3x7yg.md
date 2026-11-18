# Unit 5B Task 5 — Example solution

Demonstrate operator overloading.

```python
# Example solution: operator overloading
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
print(p1 + p2)
```

[Back to hint](../../docs/hints.md#unit-5b-task-5) · [Back to lab tasks](../../docs/lab-tasks/unit5-object-oriented-programming.md)
