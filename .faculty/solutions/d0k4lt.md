# Unit 4C Task 2 — Example solution

Write data to a text file.

```python
# Example solution: write to a text file
filename = "output.txt"
text = "Learning file handling in Python."
with open(filename, "w") as file:
    file.write(text)
print("Data written to", filename)
```

[Back to hint](../../docs/hints.md#unit-4c-task-2) · [Back to lab tasks](../../docs/lab-tasks/unit4-dictionaries-and-exception-handling.md)
