# Write a program that adds the digits in a 2 digit number.
# E.g. if the input was 35, then the output should be 3 + 5 = 8.
two_digit_num = input("Type a two digit number: ")
first_digit = two_digit_num[0]
second_digit = two_digit_num[1]
result = int(first_digit) + int(second_digit)
print(result)