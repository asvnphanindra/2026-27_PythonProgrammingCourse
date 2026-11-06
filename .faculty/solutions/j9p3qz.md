# Unit 3D Task 16 — Example solution

Lambda with `map()`, `filter()`, and `reduce()`.

```python
# Example solution: lambda with map, filter, reduce
from functools import reduce

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
total = reduce(lambda a, b: a + b, numbers)

print("Squares:", squares)
print("Evens:", evens)
print("Sum:", total)
```

[Back to hint](../../docs/hints.md#unit-3d-task-16) · [Back to lab tasks](../../docs/lab-tasks.md)
