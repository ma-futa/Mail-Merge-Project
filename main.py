with open('./Input/Letters/starting_letter.txt') as letter_data:
    starting_file = letter_data.read()
    with open('./Input/Names/invited_names.txt') as names_data:
        for name in names_data.readlines():
            name = name.replace('\n', '')
            with open(f'./Output/ReadyToSend/{name}_invitation.txt', mode='w') as invitation:
                invitation.write(starting_file.replace('[name]', name))