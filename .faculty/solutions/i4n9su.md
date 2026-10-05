# Unit 2B Task 15 — Example solution

Demonstrate `pass` with a `for` loop and a `while` loop.

## Approach 1: for loop

```python
# Example solution: pass statement using a for loop
n = int(input("Enter N (use pass for multiples of 3): "))

for number in range(1, n + 1):
    if number % 3 == 0:
        # placeholder: no action for multiples of 3
        pass
        print(f"Used pass for multiple of 3: {number} (N is {n})")
    else:
        print(f"for loop number = {number} (up to {n})")
```

## Approach 2: while loop

```python
# Example solution: pass statement using a while loop
n = int(input("Enter N (use pass for multiples of 3): "))

number = 1
while number <= n:
    if number % 3 == 0:
        # placeholder: no action for multiples of 3
        pass
        print(f"Used pass for multiple of 3: {number} (N is {n})")
    else:
        print(f"while loop number = {number} (up to {n})")
    number = number + 1
```

[Back to hint](../../docs/hints.md#unit-2b-task-15-approach-1) · [Back to lab tasks](../../docs/lab-tasks.md)
