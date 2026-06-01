from pathlib import Path

file_path = Path(__file__).with_name("file1.txt")
file_path_2 = Path(__file__).with_name("file2.txt")

with open(file_path) as file:
    contents_1 = file.readlines()

with open(file_path_2) as file:
    contents_2 = file.readlines()

result = [int(num) for num in contents_1 if num in contents_2]
print(result)