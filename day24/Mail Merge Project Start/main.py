#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
import os

input_dir = './Input'
starting_letter = os.path.join(input_dir, 'Letters', 'starting_letter.txt')
names = os.path.join(input_dir, 'Names', 'invited_names.txt')

with open(starting_letter, 'r') as f:
    letters = f.readlines()

with open(names, 'r') as f:
    names = f.readlines()

for name in names:
    output = f'letter_to_{name.strip()}.txt'
    content = letters[:]
    content[0] = content[0].replace('[name]', name.strip())
    with open(output, 'w') as f:
        f.write(''.join(content))