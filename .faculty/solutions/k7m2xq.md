# Unit 2B Task 1 — Example solution

Print numbers from 1 to N. Both approaches below.

## Approach 1: for loop

```python
# Example solution: print numbers from 1 to N using a for loop
n = int(input("Enter the value of N: "))

for number in range(1, n + 1):
    print(f"{number}")
```

## Approach 2: while loop

```python
# Example solution: print numbers from 1 to N using a while loop
n = int(input("Enter the value of N: "))

number = 1
while number <= n:
    print(f"{number}")
    number = number + 1
```

[Back to hint](../../docs/hints.md#unit-2b-task-1-approach-1) · [Back to lab tasks](../../docs/lab-tasks.md)
