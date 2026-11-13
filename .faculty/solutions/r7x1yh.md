# Unit 4A Task 7 — Example solution

Dictionary comprehension.

```python
# Example solution: dictionary comprehension
squares = {x: x * x for x in range(1, 6)}
print("Squares dict:", squares)

even_squares = {x: x * x for x in range(1, 11) if x % 2 == 0}
print("Even squares:", even_squares)
```

[Back to hint](../../docs/hints.md#unit-4a-task-7) · [Back to lab tasks](../../docs/lab-tasks/unit4-dictionaries-and-exception-handling.md)
