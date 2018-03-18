megan = {'first_name': 'megan', 'last_name': 'ingalls', 'age':3, 
	'city': 'seattle'}



peoples = {
	'megan': {
		'first': 'megan',
		'last': 'ingalls',
		'age': "23",
		},
	'devon': {
		'first': 'devon',
		'last': 'gy',
		'age': "24",
		},
	'gabi': {
		'first': 'gabi',
		'last': 'gy',
		'age': "18",
		},
	'dominic': {
		'first': 'dominic',
		'last': 'gy',
		'age': "22",
		},
	}
for people, people_info in peoples.items():
	print(people)
	full_name = people_info['first'] + " " + people_info['last']
	age = people_info['age']
	
	print("\tFullname: " + full_name.title())
	print("\tAge: " + age.title()) 
