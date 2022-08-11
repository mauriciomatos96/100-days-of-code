import pandas as pd

nato_data_frame = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dictionary = {row.letter:row.code for (index, row) in nato_data_frame.iterrows()}

def generate_phonetic():
    word = input("What is your word? ").upper()
    try:
        output_list = [nato_dictionary[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()

# have_numbers = True
# while have_numbers:
#     word = input("What is your word? ").upper()
#     for letter in word:
#         try:
#             print(f"{letter} for {nato_dictionary[letter]}")
#         except KeyError:
#             print("Sorry, only letters in the alphabet please.")
#             break
#         else:
#             have_numbers = False
