# How many days, weeks, months, and years do you have left until 90?

age = int(input("What is your current age? "))

years_remaining = 90 - age
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

print(f"You have {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months left and {years_remaining} years left.")