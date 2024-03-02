import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

dictionary = {row.letter:row.code for (index, row) in df.iterrows()}
print(dictionary)

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        result = [dictionary[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters inthe alphabet please.")
        generate_phonetic()
    else:
        print(result)

generate_phonetic()