# Error in Code
year = int(input("What's your year of birth? "))

if year > 1980 and year < 1994:
    print("You'r a Millenial.")
elif year > 1994:
    print("You'r a Gen Z.")

# Fix Code
year = int(input("What's your year of birth? "))

if year > 1980 and year < 1994:
    print("You'r a Millenial.")
elif year >= 1994:
    print("You'r a Gen Z.")