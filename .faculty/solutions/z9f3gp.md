# Unit 3D Task 7 — Example solution

`shopping_cart(**products)` with rupee prices and total.

```python
# Example solution: shopping_cart with **products
def shopping_cart(**products):
    total = 0
    print("Items Purchased:")
    for item, price in products.items():
        print(f"{item}: ₹{price}")
        total += price
    print(f"Total: ₹{total}")

# multiple keyword arguments
shopping_cart(apple=15, orange=12, mango=10)
```

[Back to hint](../../docs/hints.md#unit-3d-task-7) · [Back to lab tasks](../../docs/lab-tasks.md)
