# Unit 4C Task 5 — Example solution

Search and replace a word in a text file.

```python
# Example solution: search and replace in a file
filename = "sample.txt"
old_word = "Python"
new_word = "Java"

with open(filename, "r") as file:
    content = file.read()

updated = content.replace(old_word, new_word)

with open(filename, "w") as file:
    file.write(updated)

print("Replaced", old_word, "with", new_word)
```

[Back to hint](../../docs/hints/unit4-dictionaries-and-exception-handling.md#unit-4c-task-5) · [Back to lab tasks](../../docs/lab-tasks/unit4-dictionaries-and-exception-handling.md)
