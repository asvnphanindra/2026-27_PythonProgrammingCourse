# Unit 4B Task 7 — Example solution

Validate user input using exception-handling best practices (robust input).

```python
# Example solution: robust input validation (best practices)
# - small try block (only the conversion)
# - specific except ValueError (not bare except)
# - else for the success path
while True:
    try:
        number = int(input("Enter an integer: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
    else:
        break

print("You entered:", number)
```

[Back to hint](../../docs/hints/unit4-dictionaries-and-exception-handling.md#unit-4b-task-7) · [Back to lab tasks](../../docs/lab-tasks/unit4-dictionaries-and-exception-handling.md)
