# Quick verification of Unit 1 Task 1-15 sample inputs/outputs from docs/hints.md

print("=== Task 1: Sum of two numbers ===")
number1 = 10
number2 = 20
sum_of_numbers = number1 + number2
print(f"Expected: 30 | Match: {sum_of_numbers == 30}")
print()

print("=== Task 2: Square of a number ===")
number = 5
square_of_number = number ** 2
print(f"Expected: 25 | Match: {square_of_number == 25}")
print()

print("=== Task 3: Area and perimeter of a rectangle ===")
length_in_cm = 10
breadth_in_cm = 5
area_in_square_cm = length_in_cm * breadth_in_cm
perimeter_in_cm = 2 * (length_in_cm + breadth_in_cm)
print(f"Expected: area=50, perimeter=30 | Match: {area_in_square_cm == 50 and perimeter_in_cm == 30}")
print()

print("=== Task 4: Celsius to Fahrenheit ===")
temperature_in_celsius = 25
temperature_in_fahrenheit = (temperature_in_celsius * 9 / 5) + 32
print(f"Expected: 77 | Match: {temperature_in_fahrenheit == 77}")
print()

print("=== Task 5: Swap two numbers ===")
number1 = 10
number2 = 20
a1, a2 = number2, number1
b1, b2 = 10, 20
b1 = b1 + b2
b2 = b1 - b2
b1 = b1 - b2
print(f"Expected: 20, 10 | Match: {a1 == 20 and a2 == 10 and b1 == 20 and b2 == 10}")
print()

print("=== Task 6: Simple interest ===")
simple_interest_in_rupees = (10000 * 5 * 2) / 100
print(f"Expected: 1000 | Match: {simple_interest_in_rupees == 1000}")
print()

print("=== Task 7: Compound interest ===")
total_amount_in_rupees = 10000 * (1 + 5 / 100) ** 2
compound_interest_in_rupees = total_amount_in_rupees - 10000
print(
    f"Expected: 11025, 1025 | Match: "
    f"{total_amount_in_rupees == 11025 and compound_interest_in_rupees == 1025}"
)
print()

print("=== Task 8: Sum of first N natural numbers ===")
n = 10
sum_of_natural_numbers = n * (n + 1) / 2
print(f"Expected: 55 | Match: {sum_of_natural_numbers == 55}")
print()

print("=== Task 9: Arithmetic operators ===")
number1, number2 = 10, 3
ok = (
    number1 + number2 == 13
    and number1 - number2 == 7
    and number1 * number2 == 30
    and abs(number1 / number2 - 3.3333333333333335) < 1e-9
    and number1 // number2 == 3
    and number1 % number2 == 1
    and number1 ** number2 == 1000
)
print(f"Expected ops match | Match: {ok}")
print()

print("=== Task 10: Relational operators ===")
number1, number2 = 10, 20
ok = (
    (number1 == number2) is False
    and (number1 != number2) is True
    and (number1 > number2) is False
    and (number1 < number2) is True
    and (number1 >= number2) is False
    and (number1 <= number2) is True
)
print(f"Expected comparisons match | Match: {ok}")
print()

print("=== Task 11: Logical operators ===")
number1, number2 = 10, 20
ok = (
    ((number1 > 5) and (number2 > 15)) is True
    and ((number1 > 50) or (number2 > 15)) is True
    and (not (number1 > 50)) is True
)
print(f"Expected logical results match | Match: {ok}")
print()

print("=== Task 12: Identity operators ===")
list_a = [1, 2, 3]
list_b = list_a
list_c = [1, 2, 3]
ok = (
    (list_a is list_b) is True
    and (list_a is list_c) is False
    and (list_a is not list_c) is True
    and (list_a is not list_b) is False
)
print(f"Expected identity results match | Match: {ok}")
print()

print("=== Task 13: Membership operators ===")
text = "python"
number_list = [10, 20, 30]
float_list = [1.5, 2.5, 3.5]
bool_list = [True, False]
string_list = ["hi", "bye"]
number_tuple = (1, 2, 3)
number_set = {1, 5, 9}
student = {"name": "Ada", "age": 20}
ok = (
    ("th" in text) is True
    and ("xyz" not in text) is True
    and (10 in number_list) is True
    and (3.5 in float_list) is True
    and (True in bool_list) is True
    and ("hi" in string_list) is True
    and (2 in number_tuple) is True
    and (5 in number_set) is True
    and ("name" in student) is True
    and ("Ada" not in student) is True
)
print(f"Expected membership results match | Match: {ok}")
print()

print("=== Task 14: Operator precedence and associativity ===")
ok = (2 + 3 * 4 == 14) and (2 ** 3 ** 2 == 512) and (10 - 4 - 2 == 4)
print(f"Expected: 14, 512, 4 | Match: {ok}")
print()

print("=== Task 15: Type conversion ===")
str_num = "25"
int_num = int(str_num)
float_num = float(str_num)
str_num = str(int_num)
ok = int_num == 25 and float_num == 25.0 and str_num == "25"
print(f"Expected conversions match | Match: {ok}")
print()

print("=== Unit 2A Task 1: Valid triangle ===")
angle1_in_degrees, angle2_in_degrees, angle3_in_degrees = 60, 60, 60
is_valid = (
    angle1_in_degrees > 0
    and angle2_in_degrees > 0
    and angle3_in_degrees > 0
    and angle1_in_degrees + angle2_in_degrees + angle3_in_degrees == 180
)
invalid_sum = 90 + 90 + 90
print(f"Expected valid True, invalid sum 270 | Match: {is_valid is True and invalid_sum == 270}")
print()

print("=== Unit 2A Task 2: Voting eligibility ===")
age_in_years = 20
eligible = age_in_years >= 18
not_eligible = 16 >= 18
print(f"Expected eligible True / 16 False | Match: {eligible is True and not_eligible is False}")
print()

print("=== Unit 2A Task 3: Positive, negative, or zero ===")
number = 15
label = "positive" if number > 0 else "negative" if number < 0 else "zero"
print(f"Expected positive | Match: {label == 'positive'}")
