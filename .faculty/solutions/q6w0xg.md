# Unit 4A Task 6 — Example solution

List comprehension: squares and even numbers.

```python
# Example solution: list comprehension
numbers = range(1, 11)

squares = [x * x for x in numbers]
evens = [x for x in numbers if x % 2 == 0]

print("Squares:", squares)
print("Evens:", evens)
```

[Back to hint](../../docs/hints.md#unit-4a-task-6) · [Back to lab tasks](../../docs/lab-tasks/unit4-dictionaries-and-exception-handling.md)
