# Unit 3C Task 2 — Example solution

Set membership testing and methods: add, remove, discard.

```python
# Example solution: set membership and methods
set_data = {10, 20, 30}
print("Set:", set_data)

print("20 in set?", 20 in set_data)
print("40 not in set?", 40 not in set_data)

set_data.add(40)
print("After add:", set_data)

set_data.remove(10)
print("After remove:", set_data)

set_data.discard(99)
print("After discard:", set_data)
```

[Back to hint](../../docs/hints.md#unit-3c-task-2) · [Back to lab tasks](../../docs/lab-tasks.md)
