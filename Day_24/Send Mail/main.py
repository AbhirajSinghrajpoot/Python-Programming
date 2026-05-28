from pathlib import Path

PLACEHOLDER = "[name]"

BASE_DIR = Path(__file__).parent

name_file = BASE_DIR / "Input" / "Names" / "invited_names.txt"

with open(name_file) as file:
    names = file.readlines()

letter_file = BASE_DIR / "Input" / "Letters" / "starting_letter.docx"

with open(letter_file) as file:
    letter_contents = file.read()

for name in names:
    stripped_name = name.strip()

    new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)

    output_file = BASE_DIR / "Output" / "ReadyToSend" / f"letter_for_{stripped_name}.txt"

    with open(output_file, mode="w") as completed_letter:
        completed_letter.write(new_letter)