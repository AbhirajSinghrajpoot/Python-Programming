# For Loop

numbers = [1,2,3,4,5]
new_list = []
for n in numbers:
    added_n = n + 1
    new_list.append(added_n)
print(new_list)


# List Comprehension
new_list = [n + 1 for n in numbers]
print(new_list)


# With a String
name = "Angela"
letters_list = [letter for letter in name]
print(letters_list)

# With a Range
range_list = [n * 2 for n in range(1,5)]
print(range_list)


# With an If statement or Conditional List Comprehension

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)


long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)

