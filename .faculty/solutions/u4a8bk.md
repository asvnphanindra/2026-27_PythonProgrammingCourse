# Unit 3D Task 1 — Example solution

Rectangle area and perimeter using a function with parameters and return values.

```python
# Example solution: rectangle area and perimeter (function)
def rectangle_area_perimeter(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    return area, perimeter

length = 5
breadth = 3
area, perimeter = rectangle_area_perimeter(length, breadth)
print("Area:", area)
print("Perimeter:", perimeter)
```

[Back to hint](../../docs/hints.md#unit-3d-task-1) · [Back to lab tasks](../../docs/lab-tasks.md)
