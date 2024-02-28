import pandas

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

df = pandas.read_csv("nato_phonetic_alphabet.csv")

dictionary = {row.letter:row.code for (index, row) in df.iterrows()}
print(dictionary)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ").upper()
result = [dictionary[letter] for letter in word]
print(result)