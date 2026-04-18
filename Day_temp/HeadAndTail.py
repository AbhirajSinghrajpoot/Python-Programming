import random

testSeed = int(input("Create a seed number: "))
random.seed(testSeed)
random_choice = random.randint(0, 1)
if random_choice == 0:
    print("Head")
else:
    print("Tail")