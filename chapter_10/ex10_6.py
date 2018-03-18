print("Give me two numbers to add!")
print("Enter 'q' to quit.")

while True:
    first_number = input('\nFirst Number: ')
    if first_number == 'q':
        break
    second_number = input('\nSecond Number: ')
    try:
        answer = int(first_number) + int(second_number)
    except TypeError:
        print("Whoops, looks like you didn't put in a number!")
    except ValueError:
        print("Whoops, looks like you didn't put in a number!")
    else:
        print(answer)
