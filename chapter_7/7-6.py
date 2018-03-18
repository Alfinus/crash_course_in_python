#three exits
#A while statement that stops the loop
#an active variable to control how long the loop runs
#A break statement to exit the loop when the user enters 'quit'


print("\nEnter 'quit' to end the program. ")
prompt = '\nHow old are you? '

active = True

while active:
	age = input(prompt)
	
	if age == 'quit':
		break
	else:
		age = int(age)
		if age >= 12:
			age = str(age)
			print("\nSince your age is " + age.title() + " we will charge you $15)")
		elif age < 12 and age >= 3:
			age = str(age)
			print("\nSince your age is " + age.title() + " we will charge you $10")
		elif age < 3:
			age = str(age)
			print("\nSince you are " + age.title() + " you are free of charge")
		
	
		
	


			
	
	


