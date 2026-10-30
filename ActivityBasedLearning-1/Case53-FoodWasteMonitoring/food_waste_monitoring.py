# Case 53: Food Waste Monitoring System
# INPUT -> PROCESS -> OUTPUT

print("Food Waste Monitoring")

# ----- INPUT -----
int_days = int(input("Number of days: "))
float_limit = float(input("Acceptable limit %: "))

list_high_waste_days = []

print("\n--- OUTPUT ---")
print("Day\tPrepared\tLeftovers\tWastage%\tStatus")

for i in range(int_days):
    # ----- INPUT (each day) -----
    str_day = input("\nDay name: ")
    int_prepared = int(input("Meals prepared: "))
    int_leftovers = int(input("Leftovers: "))

    # ----- PROCESS -----
    float_waste = (int_leftovers / int_prepared) * 100
    if float_waste > float_limit:
        str_status = "HIGH WASTE"
        list_high_waste_days.append(str_day)
    else:
        str_status = "OK"

    # ----- OUTPUT (each day) -----
    print(f"{str_day}\t{int_prepared}\t\t{int_leftovers}\t\t{round(float_waste, 2)}\t{str_status}")

# ----- OUTPUT (summary) -----
print(f"\nDays with high waste: {list_high_waste_days}")
