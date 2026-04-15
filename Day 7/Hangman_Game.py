import random

stages = ['''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
''', '''
    +---+
    |   |
    O   |
        |
        |
        |
''', '''
    +---+
    |   |
        |
        |
        |
        |
''']


from Hangman_word import word_list

chosen_word = random.choice(word_list)
word_lenght = len(chosen_word)
end_of_game = False
lives = 6

print(f"The chosen word is {chosen_word}")
display = []
for _ in range(word_lenght):
    display += "_"


while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win.")
    
    from hangman_art import logo
    print(stages[lives])
