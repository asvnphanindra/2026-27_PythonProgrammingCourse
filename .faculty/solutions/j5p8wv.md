# Unit 2A Task 8 — Example solution

Check whether a number is prime or not (input must be between 1 and 100).

```python
# Example solution: prime number check for a value between 1 and 100
number = int(input("Enter a number between 1 and 100: "))

if number < 1 or number > 100:
    print(f"{number} is not between 1 and 100")
else:
    if number == 1:
        print(f"{number} is not a prime number")
    else:
        is_prime = True

        for divisor in range(2, number):
            if number % divisor == 0:
                is_prime = False
                break

        if is_prime:
            print(f"{number} is a prime number")
        else:
            print(f"{number} is not a prime number")
```
