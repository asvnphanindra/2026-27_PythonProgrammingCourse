# Unit 3D Task 9 — Example solution

Product order using both `*args` and `**kwargs`.

```python
# Example solution: product order with *args and **kwargs
def print_order(*args, **kwargs):
    print("Items:")
    for item in args:
        print("-", item)
    print("Details:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_order("pen", "notebook", qty=2, price=50)
```

[Back to hint](../../docs/hints.md#unit-3d-task-9) · [Back to lab tasks](../../docs/lab-tasks.md)
