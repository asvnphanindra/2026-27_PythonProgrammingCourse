# Case 53: Food Waste Monitoring System
# INPUT -> PROCESS -> OUTPUT

print("Food Waste Monitoring")

# ----- INPUT -----
n = int(input("Number of days: "))
limit = float(input("Acceptable limit %: "))

high_waste_days = []

print("\n--- OUTPUT ---")
print("Day\tPrepared\tLeftovers\tWastage%\tStatus")

for i in range(n):
    # ----- INPUT (each day) -----
    day = input("\nDay name: ")
    prepared = int(input("Meals prepared: "))
    leftovers = int(input("Leftovers: "))

    # ----- PROCESS -----
    waste = (leftovers / prepared) * 100
    if waste > limit:
        status = "HIGH WASTE"
        high_waste_days.append(day)
    else:
        status = "OK"

    # ----- OUTPUT (each day) -----
    print(f"{day}\t{prepared}\t\t{leftovers}\t\t{round(waste, 2)}\t{status}")

# ----- OUTPUT (summary) -----
print(f"\nDays with high waste: {high_waste_days}")
