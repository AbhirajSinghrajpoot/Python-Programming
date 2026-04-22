# BMI is calculated by dividing a person's weight (in kg)
# by the square of their height (in m): BMI = weight / height^2
# Warning: round the result to the nearest whole number.

Weight = input("What is your weight? ")
height = input("What is your height? ")

bmi = int(Weight) / float(height) ** 2
print(int(bmi))