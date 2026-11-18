# Unit 5B Task 2 — Example solution

Demonstrate multiple and multilevel inheritance.

```python
# Example solution: multilevel and multiple inheritance
# Multilevel: A -> B -> C
class A:
    def feature_a(self):
        print("Feature A")


class B(A):
    def feature_b(self):
        print("Feature B")


class C(B):
    def feature_c(self):
        print("Feature C")


# Multiple: Child inherits Father and Mother
class Father:
    def skill_f(self):
        print("Father skill")


class Mother:
    def skill_m(self):
        print("Mother skill")


class Child(Father, Mother):
    pass


obj = C()
obj.feature_a()
obj.feature_b()
obj.feature_c()

ch = Child()
ch.skill_f()
ch.skill_m()
```

[Back to hint](../../docs/hints.md#unit-5b-task-2) · [Back to lab tasks](../../docs/lab-tasks/unit5-object-oriented-programming.md)
