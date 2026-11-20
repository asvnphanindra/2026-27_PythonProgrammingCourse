# Unit 4B Task 6 — Example solution

Raise `InvalidSpeedError` when vehicle speed is outside 0–120 km/h.

```python
# Example solution: InvalidSpeedError for vehicle speed
class InvalidSpeedError(Exception):
    pass


try:
    speed = int(input("Enter speed (km/h): "))
    if speed < 0 or speed > 120:
        raise InvalidSpeedError("Speed must be between 0 and 120.")
    print("Speed accepted:", speed)
except InvalidSpeedError as err:
    print("Custom error:", err)
except ValueError:
    print("Please enter a valid integer.")
```

[Back to hint](../../docs/hints/unit4-dictionaries-and-exception-handling.md#unit-4b-task-6) · [Back to lab tasks](../../docs/lab-tasks/unit4-dictionaries-and-exception-handling.md)
