# Tip Calculator: Calculate total bill with tip percentage and split among people.
# Take bill amount, tip percentage (10, 12, or 15%), and number of people to split.
# Formula: total_bill = bill + (bill * tip_percentage / 100), then divide by people.

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

total_bill = bill + (bill * tip / 100)
amount_per_person = total_bill / people

print(f"Each person should pay: ${amount_per_person:.2f}")