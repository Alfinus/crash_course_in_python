filename = 'guest.txt'

print('/please enter your first name')
f_name = input("First Name: ")
l_name = input("Last Name: ")


with open(filename, 'w') as file_object:
    file_object.write (f_name + ' ')
with open(filename,'a') as file_object:
    file_object.write (l_name + ' ')
