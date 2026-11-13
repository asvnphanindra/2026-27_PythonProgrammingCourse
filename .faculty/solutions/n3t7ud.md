# Unit 4A Task 3 — Example solution

Word frequency using a dictionary.

```python
# Example solution: word frequency dictionary
sentence = "to be or not to be"
words = sentence.split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print("Frequency:", freq)
```

[Back to hint](../../docs/hints.md#unit-4a-task-3) · [Back to lab tasks](../../docs/lab-tasks/unit4-dictionaries-and-exception-handling.md)
