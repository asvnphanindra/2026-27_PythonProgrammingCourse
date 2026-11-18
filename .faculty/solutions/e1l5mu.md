# Unit 4C Task 3 — Example solution

Count words, lines and characters in a text file.

```python
# Example solution: count lines, words, characters
filename = "sample.txt"
with open(filename, "r") as file:
    text = file.read()

line_count = len(text.splitlines()) if text else 0
word_count = len(text.split())
char_count = len(text)

print("Lines:", line_count)
print("Words:", word_count)
print("Characters:", char_count)
```

[Back to hint](../../docs/hints.md#unit-4c-task-3) · [Back to lab tasks](../../docs/lab-tasks/unit4-dictionaries-and-exception-handling.md)
