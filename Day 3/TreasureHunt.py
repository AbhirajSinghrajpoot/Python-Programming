print(r'''
*******************************************************************************
		  |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,"-_,=""     `"=.|                  |
|___________________|__"=._o`-._        `"=.______________|___________________
		  |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".     |
|___________________|_._"  ,. .` ` `` ,  `-.o."-._   ; `.     |_______________
		  |           |o` "=._`_.; ;. _.-""--._`"=.o.___   ;   |
 _________|___________|__; ;`,'_..--  .""-._   `"=._o  _,'"---._;___|_________
|                   |o/ ;  `."`'  `-._   "--._   _."o|      |
|___________________|__|o;    `. "`_.--"`.   _..--"/o_|______________________
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input('You are at a crossroad. Where do you want to go? Type "left" or "right": ').lower()

if choice1 == "left":
	choice2 = input('You have come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat or "swim" to swim across: ').lower()

	if choice2 == "wait":
		choice3 = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ').lower()

		if choice3 == "yellow":
			print("You found the treasure! You win!")
		elif choice3 == "red":
			print("It is a room full of fire. Game Over.")
		elif choice3 == "blue":
			print("You enter a room of beasts. Game Over.")
		else:
			print("You chose a door that doesn't exist. Game Over.")
	else:
		print("You got attacked by an angry trout. Game Over.")
else:
	print("You fell into a hole. Game Over.")
