
guest_list = ['triss', 'geralt', 'zykon', 'bill']

print ('hello ' + guest_list[0] + " do you want to party?")
print ('hello ' + guest_list[1] + " do you want to party?")
print ('hello ' + guest_list[-1] + " do you want to party?")

print ('unfortunately ' + guest_list[1] + ' cannot make it to the party')

guest_list.remove('geralt')
guest_list.append('shani')

print (guest_list)

print ('well...' + guest_list[0] + ' still wannt come to the party?')
print ('well...' + guest_list[1] + ' still wannt come to the party?')
print ('well...' + guest_list[-1] + ' still wannt come to the party?')

