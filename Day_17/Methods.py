class User:
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name
        self.followers = 0
        
    def follow(self, user):
        user.followers += 1
        self.followers += 1
        
user1 = User(1, "Alice")
user2 = User(2, "Bob")

print(user1.user_id)  # Output: 1
print(user1.user_name)  # Output: Alice
print(user1.followers)  # Output: 0
user1.follow(user2)
print(user2.user_id)  # Output: 2
print(user2.user_name)  # Output: Bob
print(user2.followers)  # Output: 1