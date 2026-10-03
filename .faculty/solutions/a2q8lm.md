# Unit 2A Task 1 — Example solution

Check whether a triangle is valid from three angles.

```python
# Example solution: valid triangle from three angles
angle1_in_degrees = float(input("Enter first angle in degrees: "))
angle2_in_degrees = float(input("Enter second angle in degrees: "))
angle3_in_degrees = float(input("Enter third angle in degrees: "))

if (
    angle1_in_degrees > 0
    and angle2_in_degrees > 0
    and angle3_in_degrees > 0
    and angle1_in_degrees + angle2_in_degrees + angle3_in_degrees == 180
):
    print(
        f"The triangle with angles {angle1_in_degrees}, "
        f"{angle2_in_degrees}, and {angle3_in_degrees} is valid"
    )
else:
    print(
        f"The triangle with angles {angle1_in_degrees}, "
        f"{angle2_in_degrees}, and {angle3_in_degrees} is not valid"
    )
```
