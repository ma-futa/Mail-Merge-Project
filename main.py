# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


starting_file = ''
with open('./Input/Letters/starting_letter.txt') as letter_data:
    starting_file = letter_data.read()
    with open('./Input/Names/invited_names.txt') as names_data:
        for name in names_data.readlines():
            name = name.replace('\n', '')
            with open(f'./Output/ReadyToSend/{name}_invitation.txt', mode='w') as invitation:
                invitation.write(starting_file.replace('[name]', name))



