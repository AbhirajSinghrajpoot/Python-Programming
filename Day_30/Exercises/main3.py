import pandas as pd
import pathlib

data = pd.read_csv(pathlib.Path("./Day_30/Exercises/nato_phonetic_alphabet.csv"))

phonetic_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_alphabet)

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_alphabet[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)
        
generate_phonetic()