# Unit 4B Task 2 — Example solution

Handle multiple exceptions using multiple except blocks.

```python
# Example solution: multiple except blocks
list_data = [10, 20, 30]
try:
    index = int(input("Enter index: "))
    value = list_data[index]
    print("Value:", value)
except ValueError:
    print("Please enter a valid integer index.")
except IndexError:
    print("Index is out of range.")
```

[Back to hint](../../docs/hints.md#unit-4b-task-2) · [Back to lab tasks](../../docs/lab-tasks/unit4-dictionaries-and-exception-handling.md)
