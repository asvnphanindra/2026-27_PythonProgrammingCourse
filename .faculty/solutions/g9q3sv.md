# Unit 2D Task 7 — Example solution

Count the frequency of each character.

```python
# Example solution: character frequency
s = input("Enter a string: ")

frequency = {}

for ch in s:
    if ch in frequency:
        frequency[ch] = frequency[ch] + 1
    else:
        frequency[ch] = 1

for ch, count in frequency.items():
    print(ch, ":", count)
```

[Back to hint](../../docs/hints.md#unit-2d-task-7) · [Back to lab tasks](../../docs/lab-tasks.md)
