# Unit 4B Task 3 — Example solution

Convert text to an integer, print its square in `else`, and always print Program finished in `finally`.

```python
# Example solution: try-except-else-finally (square of an integer)
try:
    text = input("Enter a number: ")
    number = int(text)
except ValueError:
    print("That is not a valid integer.")
else:
    print("Square:", number * number)
finally:
    print("Program finished.")
```

[Back to hint](../../docs/hints/unit4-dictionaries-and-exception-handling.md#unit-4b-task-3) · [Back to lab tasks](../../docs/lab-tasks/unit4-dictionaries-and-exception-handling.md)
