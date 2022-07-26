import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

word = input("Please enter a word.").upper()
codes = [phonetic_dict[letter] for letter in word]
print(codes)
