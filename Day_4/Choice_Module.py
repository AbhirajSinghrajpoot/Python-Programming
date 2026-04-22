import random

testSeed = int(input("Create a seed number: "))
random.seed(testSeed)

namesAsCSV = input("Give me everybody's names, separated by a comma. ")
names = namesAsCSV.split(", ")

person_who_will_pay = random.choice(names)
print(f"{person_who_will_pay} is going to buy the meal today!")