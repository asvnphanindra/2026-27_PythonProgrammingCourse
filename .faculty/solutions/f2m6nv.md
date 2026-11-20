# Unit 4C Task 4 — Example solution

Copy the content of sample.txt into copy.txt.

```python
# Example solution: copy file content
source = "sample.txt"
destination = "copy.txt"
with open(source, "r") as src:
    content = src.read()
with open(destination, "w") as dest:
    dest.write(content)
print("Copied from", source, "to", destination)
```

[Back to hint](../../docs/hints/unit4-dictionaries-and-exception-handling.md#unit-4c-task-4) · [Back to lab tasks](../../docs/lab-tasks/unit4-dictionaries-and-exception-handling.md)
