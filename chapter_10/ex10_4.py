# Write a while loop that prompts users for their nameself.
#Then Print a greeting for their name and add a line recording
#their visit in a file called guest_book.txt


filename = 'guest_book.txt'

message = 'Hello and welcome to the program '

while True:
    prompt = print('Please enter your name')

    f_name = input("First Name: ")
    if f_name == 'q':
            break
    l_name = input("Last Name: ")
    if l_name == 'q':
        break
    print(message + f_name.title() + ' ' +
    l_name.title() + '!')

    with open(filename,'a') as file_object:
        file_object.write (f_name + ' ')
        file_object.write (l_name + ' \n')
