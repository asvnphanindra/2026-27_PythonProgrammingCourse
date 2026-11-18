# Unit 5A Task 4 — Example solution

Demonstrate encapsulation using private and protected attributes.

```python
# Example solution: private and protected attributes
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._branch = "Main"  # protected (convention)
        self.__balance = balance  # private (name-mangled)

    def get_balance(self):
        return self.__balance


acc = BankAccount("Sita", 1000)
print(acc.owner, acc._branch)
print("Balance:", acc.get_balance())
```

[Back to hint](../../docs/hints.md#unit-5a-task-4) · [Back to lab tasks](../../docs/lab-tasks/unit5-object-oriented-programming.md)
