#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines() #Names extracted from the inivted names file as a list using .readlines() method


with open("./Input/Letters/starting_letter.txt") as letter_file: 
    letter_contents = letter_file.read() #Opening template file, and saving the contents
    for name in names:
        stripped_name = name.strip() #Looping through the names and removing spaces with .strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name) #Replacing the [name] line with actual names from the list
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", "w") as completed_letter: #Creating a new files for each name
            completed_letter.write(new_letter) #Writing that new file with the contents of new_letter