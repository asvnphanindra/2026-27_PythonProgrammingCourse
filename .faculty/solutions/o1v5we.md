# Unit 5B Task 3 — Example solution

Demonstrate method overriding using inheritance.

```python
# Example solution: method overriding
class Animal:
    def sound(self):
        print("Some sound")


class Dog(Animal):
    def sound(self):
        print("Bark")


a = Animal()
d = Dog()
a.sound()
d.sound()
```

[Back to hint](../../docs/hints/unit5-object-oriented-programming.md#unit-5b-task-3) · [Back to lab tasks](../../docs/lab-tasks/unit5-object-oriented-programming.md)
