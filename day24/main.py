#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"

names_file = open("./Input/Names/invited_names.txt")
start_file = open("./Input/Letters/starting_letter.txt")
start_text = start_file.read()
start_file.close()

for name_line in names_file:
    name = name_line.strip("\n")
    content = start_text.replace(PLACEHOLDER, name)

    end_file = open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w")
    end_file.write(content)
    end_file.close()


names_file.close()