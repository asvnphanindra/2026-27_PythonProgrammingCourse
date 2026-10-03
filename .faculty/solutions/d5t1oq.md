# Unit 2A Task 5 — Example solution

Largest of three numbers using nested if.

```python
# Example solution: largest of three numbers using nested if
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

if x >= y:
    if x >= z:
        largest = x
    else:
        largest = z
else:
    if y >= z:
        largest = y
    else:
        largest = z

print(f"Largest = {largest} (among {x}, {y}, {z})")
```
