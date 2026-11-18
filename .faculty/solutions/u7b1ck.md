# Unit 5D Task 1 — Example solution

Mini application using OOP concepts (Bank Account Management).

```python
# Example solution: simple bank account mini application
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdraw amount")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print("Withdrawn:", amount)

    def display(self):
        print(f"Owner: {self.owner}, Balance: {self.__balance}")


acc = BankAccount("Krishna", 1000)
acc.display()
acc.deposit(500)
acc.withdraw(200)
acc.display()
```

> Students may instead implement a Library Management System with classes such as `Book` and `Library` (add / issue / return / list).

[Back to hint](../../docs/hints/unit5-object-oriented-programming.md#unit-5d-task-1) · [Back to lab tasks](../../docs/lab-tasks/unit5-object-oriented-programming.md)
