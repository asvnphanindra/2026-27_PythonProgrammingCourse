# Unit 4A Task 2 — Example solution

Dictionary methods: keys, values, items, get, update, pop.

```python
# Example solution: dictionary methods
data = {"a": 1, "b": 2, "c": 3}
print("Keys:", data.keys())
print("Values:", data.values())
print("Items:", data.items())
print("get b:", data.get("b"))
print("get z:", data.get("z"))

data.update({"b": 20, "d": 4})
print("After update:", data)

removed = data.pop("a")
print("Removed:", removed)
print("After pop:", data)
```

[Back to hint](../../docs/hints.md#unit-4a-task-2) · [Back to lab tasks](../../docs/lab-tasks/unit4-dictionaries-and-exception-handling.md)
