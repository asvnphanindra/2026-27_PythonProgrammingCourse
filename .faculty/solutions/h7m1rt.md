# Unit 2B Task 14 — Example solution

Demonstrate `continue` with a `for` loop and a `while` loop.

## Approach 1: for loop

```python
# Example solution: continue statement using a for loop
n = int(input("Enter N (print 1 to N, skip even numbers): "))

for number in range(1, n + 1):
    if number % 2 == 0:
        print(f"Skipping even number {number} with continue (N is {n})")
        continue
    print(f"for loop odd number = {number} (up to {n})")
```

## Approach 2: while loop

```python
# Example solution: continue statement using a while loop
n = int(input("Enter N (print 1 to N, skip even numbers): "))

number = 1
while number <= n:
    if number % 2 == 0:
        print(f"Skipping even number {number} with continue (N is {n})")
        number = number + 1
        continue
    print(f"while loop odd number = {number} (up to {n})")
    number = number + 1
```

[Back to hint](../../docs/hints.md#unit-2b-task-14-approach-1) · [Back to lab tasks](../../docs/lab-tasks.md)
