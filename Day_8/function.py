def greet():
    print("Hello, World!")
    print("Welcome to the Python programming language.")
    print("Let's have fun learning and coding together!")

greet()

# Function with input

def greet_with_name(name):
    print(f"Hello, {name}!")
    print("Welcome to the Python programming language.")
    print("Let's have fun learning and coding together!")

greet_with_name("Alice")

# Function with more than 1 input

def greet_with(name, location):
    print(f"Hello, {name}!")
    print(f"What is it like in {location}?")
    print("Let's have fun learning and coding together!")

greet_with(name = "Angela", location = "New York")