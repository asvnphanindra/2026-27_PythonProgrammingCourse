# Unit 5B Task 4 — Example solution

Demonstrate polymorphism using method overriding.

```python
# Example solution: polymorphism with method overriding
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
    s.area()
```

[Back to hint](../../docs/hints/unit5-object-oriented-programming.md#unit-5b-task-4) · [Back to lab tasks](../../docs/lab-tasks/unit5-object-oriented-programming.md)
