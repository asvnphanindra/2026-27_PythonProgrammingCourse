# Unit 3D Task 12 — Example solution

Bank balance: deposit updates global; local assignment does not.

```python
# Example solution: bank balance global vs local
balance = 1000

def deposit(amount):
    global balance
    balance = balance + amount
    print("After deposit, balance =", balance)

def show_local_balance():
    balance = 0  # local only
    print("Inside local function, balance =", balance)

print("Start:", balance)
deposit(500)
print("Account balance:", balance)
show_local_balance()
print("Account balance still:", balance)
```

[Back to hint](../../docs/hints.md#unit-3d-task-12) · [Back to lab tasks](../../docs/lab-tasks.md)
