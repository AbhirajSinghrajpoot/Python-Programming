from pathlib import Path

file_path = Path(__file__).with_name("my_file.txt")

with open(file_path) as file:
    content = file.read()
    print(content)
    
with open(file_path, mode="a") as file:
    file.write("\nThis is a new line added to the file.")
    
new_file_path = Path(__file__).with_name("new_file.txt")

with open(new_file_path, mode="w") as file:
    file.write("This is a new file.")

with open(new_file_path, mode="r") as file:
    content = file.read()
    print(content)