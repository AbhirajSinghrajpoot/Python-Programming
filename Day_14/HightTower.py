from art import logo
from game_data import data
import random
import os

def formate_data(account):
    """Take the account data into printable formate."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return (f"{account_name}, a {account_descr}, from {account_country}")

def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if the got """
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {formate_data(account_a)}.")
    print("VS")
    print(f"Against B: {formate_data(account_b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}.")