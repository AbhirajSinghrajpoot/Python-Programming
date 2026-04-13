height = float(input("What is your height in m? \n"))
weight = float(input("What is your weight in kg? \n"))

bmi = round(weight / height ** 2)

if bmi < 18.5:
    print(f'Your BMI is {int(bmi)}, you are underweight.')
elif bmi < 25:
    print(f'Your BMI is {int(bmi)}, you have a normal weight.')
elif bmi < 30:
    print(f'Your BMI is {int(bmi)}, you are overweight.')
elif bmi < 35:
    print(f'Your BMI is {int(bmi)}, you are obese.')
else:
    print(f'Your BMI is {int(bmi)}, you are clinically obese.')
