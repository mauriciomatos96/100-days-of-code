#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

all_guessed = []

with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()

with open("Input/Names/invited_names.txt", "r") as name_files:
    names = name_files.readlines()



for guest in names:
    all_guessed.append(guest.strip("\n"))


for invited in all_guessed:
    with open(f"Output/ReadyToSend/letter_for_{invited}.txt", "w") as letter:
        letter.write(letter_content.replace("[name]", f"{invited}"))

