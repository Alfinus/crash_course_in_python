
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

print ('i also found a bigger table... so more people will be coming!')

guest_list.insert(0,'lez')
guest_list.insert(2,'donniven')
guest_list.append('janis')

print ('hello ' + guest_list[0] + " do you want to party?")
print ('hello ' + guest_list[-1] + " do you want to party?")
print ('hello ' + guest_list[2] + " do you want to party?")

print('\nSo I made a mistake... I can only invite two people...')

print (guest_list)

sorry0 = guest_list.pop(0)
print ('sorry ' + sorry0 + ' you cant come to my party')
sorry1 = guest_list.pop(2)
print ('sorry ' + sorry1 + ' you cant come to my party')
sorry2 = guest_list.pop(3)
print ('sorry ' + sorry2 + ' you cant come to my party')

