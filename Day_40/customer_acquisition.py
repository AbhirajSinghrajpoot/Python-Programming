import requests

SHEETY_USERS_ENDPOINT = "https://api.sheety.co/421e6d158f355f5e0c0f10b88fdb3f1f/flightDeals/users"

headers = {
    "Authorization": "Bearer flightDealsToken123"
}

print("Welcome to Abhiraj's Flight Club.")
print("We find the best flight deals and email you.\n")

first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")

email = input("What is your email?\n")
confirm_email = input("Type your email again.\n")

if email == confirm_email:

    user_data = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email
        }
    }

    response = requests.post(
        url=SHEETY_USERS_ENDPOINT,
        json=user_data,
        headers=headers
    )

    print("You're in the club!")

else:
    print("Emails do not match.")