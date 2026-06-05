import datetime as dt

now = dt.datetime.now()

year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second
print(f"Current date and time: {now}")
print(f"Year: {year}")
print(f"Month: {month}")
print(f"Day: {day}")
print(f"Hour: {hour}")
print(f"Minute: {minute}")
print(f"Second: {second}")
# Create a specific date and time

specific_date = dt.datetime(2022, 1, 1, 12, 0, 0)
print(f"Specific date and time: {specific_date}")
# Format the date and time
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted current date and time: {formatted_date}")
# Calculate the difference between two dates
date1 = dt.datetime(2022, 1, 1)
date2 = dt.datetime(2022, 12, 31)
date_difference = date2 - date1
print(f"Difference between {date2} and {date1}: {date_difference.days} days")
# Add 7 days to the current date
future_date = now + dt.timedelta(days=7)
print(f"Date after adding 7 days: {future_date}")
# Subtract 30 minutes from the current time
past_time = now - dt.timedelta(minutes=30)
print(f"Time after subtracting 30 minutes: {past_time}")


date_of_birth = dt.datetime(1990, 5, 15)
today = dt.datetime.now()
print(f"Date of Birth: {date_of_birth}")
print(f"Today: {today}")