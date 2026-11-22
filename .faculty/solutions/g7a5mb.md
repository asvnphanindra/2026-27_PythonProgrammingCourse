# Unit 1 Task 13 — Example solution

Demonstrate membership operators in and not in.

```python
# Example solution: membership operators
# string
text = "python"
print(f"'th' in '{text}' is {'th' in text}")
print(f"'xyz' not in '{text}' is {'xyz' not in text}")

# list (int, float, bool, str values)
number_list = [10, 20, 30]
float_list = [1.5, 2.5, 3.5]
bool_list = [True, False]
string_list = ["hi", "bye"]
print(f"10 in {number_list} is {10 in number_list}")
print(f"3.5 in {float_list} is {3.5 in float_list}")
print(f"True in {bool_list} is {True in bool_list}")
print(f"'hi' in {string_list} is {'hi' in string_list}")

# tuple
number_tuple = (1, 2, 3)
print(f"2 in {number_tuple} is {2 in number_tuple}")

# set
number_set = {1, 5, 9}
print(f"5 in {number_set} is {5 in number_set}")

# dictionary (membership checks keys)
student = {"name": "Ada", "age": 20}
print(f"'name' in {student} is {'name' in student}")
print(f"'Ada' not in {student} is {'Ada' not in student}")
```

[Back to hint](../../docs/hints/unit1-python-fundamentals.md#unit-1-task-13) · [Back to lab tasks](../../docs/lab-tasks/unit1-python-fundamentals.md)
