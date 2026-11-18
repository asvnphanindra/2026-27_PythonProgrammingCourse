# Unit 4B Task 7 — Example solution

Validate user input using exception handling (robust input).

```python
# Example solution: robust input validation
while True:
    try:
        number = int(input("Enter an integer: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

print("You entered:", number)
```

[Back to hint](../../docs/hints/unit4-dictionaries-and-exception-handling.md#unit-4b-task-7) · [Back to lab tasks](../../docs/lab-tasks/unit4-dictionaries-and-exception-handling.md)
