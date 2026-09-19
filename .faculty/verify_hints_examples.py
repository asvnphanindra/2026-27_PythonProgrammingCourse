# Quick verification of Unit 1 Task 4-8 sample inputs/outputs from docs/hints.md

print("=== Task 4: Celsius to Fahrenheit ===")
temperature_in_celsius = 25
temperature_in_fahrenheit = (temperature_in_celsius * 9 / 5) + 32
print(f"Input:  temperature_in_celsius = {temperature_in_celsius}")
print(f"Output: temperature_in_fahrenheit = {temperature_in_fahrenheit}")
print(f"Expected: 77 | Match: {temperature_in_fahrenheit == 77}")
print()

print("=== Task 5: Swap two numbers ===")
number1 = 10
number2 = 20
print(f"Input:  number1 = {number1}, number2 = {number2}")

# Approach 1: tuple unpacking
a1, a2 = number1, number2
a1, a2 = a2, a1
print(f"Approach 1 output: number1 = {a1}, number2 = {a2}")

# Approach 2: arithmetic
b1, b2 = number1, number2
b1 = b1 + b2
b2 = b1 - b2
b1 = b1 - b2
print(f"Approach 2 output: number1 = {b1}, number2 = {b2}")
print(f"Expected: number1 = 20, number2 = 10 | Match: {a1 == 20 and a2 == 10 and b1 == 20 and b2 == 10}")
print()

print("=== Task 6: Simple interest ===")
principal_amount_in_rupees = 10000
rate_of_interest_in_percent = 5
time_in_years = 2
simple_interest_in_rupees = (
    principal_amount_in_rupees * rate_of_interest_in_percent * time_in_years
) / 100
print(
    f"Input:  principal={principal_amount_in_rupees}, "
    f"rate={rate_of_interest_in_percent}, time={time_in_years}"
)
print(f"Output: simple_interest_in_rupees = {simple_interest_in_rupees}")
print(f"Expected: 1000 | Match: {simple_interest_in_rupees == 1000}")
print()

print("=== Task 7: Compound interest ===")
principal_amount_in_rupees = 10000
rate_of_interest_in_percent = 5
time_in_years = 2
total_amount_in_rupees = principal_amount_in_rupees * (
    1 + rate_of_interest_in_percent / 100
) ** time_in_years
compound_interest_in_rupees = total_amount_in_rupees - principal_amount_in_rupees
print(
    f"Input:  principal={principal_amount_in_rupees}, "
    f"rate={rate_of_interest_in_percent}, time={time_in_years}"
)
print(f"Output: total_amount_in_rupees = {total_amount_in_rupees}")
print(f"Output: compound_interest_in_rupees = {compound_interest_in_rupees}")
print(
    f"Expected: total=11025, CI=1025 | Match: "
    f"{total_amount_in_rupees == 11025 and compound_interest_in_rupees == 1025}"
)
print()

print("=== Task 8: Sum of first N natural numbers ===")
n = 10  # n matches the formula
sum_of_natural_numbers = n * (n + 1) / 2
print(f"Input:  n = {n}")
print(f"Output: sum_of_natural_numbers = {sum_of_natural_numbers}")
print(f"Expected: 55 | Match: {sum_of_natural_numbers == 55}")
