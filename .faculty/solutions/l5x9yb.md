# Unit 3A Task 4 — Example solution

Remove duplicate elements from a list (preserve order with a loop).

```python
# Example solution: remove duplicates from a list
list_data = [1, 2, 2, 3, 1, 4, 3]
unique = []

for item in list_data:
    if item not in unique:
        unique.append(item)

print("Original:", list_data)
print("Without duplicates:", unique)
```

[Back to hint](../../docs/hints.md#unit-3a-task-4) · [Back to lab tasks](../../docs/lab-tasks.md)
