import random

testSeed = int(input("Create a seed number: "))
random.seed(testSeed)
randomInteger = random.randint(1, 10)
print(randomInteger)