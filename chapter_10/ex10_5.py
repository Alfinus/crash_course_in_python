#Ex 10 - 5 Reasons why they like programming

filename = 'poll.txt'

message = 'Thank you for your response!'

while True:
    print('Thank you for your time to take this poll, please type "q" when finished')
    reason = input('Please enter why you like programming: ')
    if reason == 'q':
            break

    print(message)

    with open (filename,'a') as file_object:
        file_object.write (reason + '\n')
