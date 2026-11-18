# Unit 5A Task 3 — Example solution

Demonstrate instance methods, class methods and static methods.

```python
# Example solution: instance, class, and static methods
class Demo:
    college = "RVRJC"

    def set_name(self, name):
        self.name = name
        print("Instance:", self.name)

    @classmethod
    def show_college(cls):
        print("Class:", cls.college)

    @staticmethod
    def info():
        print("Static: utility message")


obj = Demo()
obj.set_name("Anu")
Demo.show_college()
Demo.info()
```

[Back to hint](../../docs/hints/unit5-object-oriented-programming.md#unit-5a-task-3) · [Back to lab tasks](../../docs/lab-tasks/unit5-object-oriented-programming.md)
