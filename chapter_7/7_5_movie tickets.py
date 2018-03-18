#movie tickets
#need to make 3 seperate clauses with a prompt asking for age

age = input("So how old are you? ")
age = int(age)

if age >= 12:
	age = str(age)
	print("Since your age is " + age.title() + " we will charge you $15")
elif age < 12 and age >= 3:
	age = str(age)
	print("Since your age is " + age.title() + " we will charge you $10")
else:
	age = str(age)
	print("Since you are " + age.title() + " you are free of charge")
		
