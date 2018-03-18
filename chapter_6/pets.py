# several dictionaries containing pets and informatoin about said pets


pets = {
	'cinnamon': {
		'kind': 'dog',
		'owner': 'gy family',
		},
	'coco': {
		'kind': 'dog',
		'owner': 'gy family',
		},
	'zorra': {
		'kind': 'cat',
		'owner': 'ingalls family',
		},
	'puddles': {
		'kind': 'dog',
		'owner': ' dani and libby',
		},
	'chowder': {
		'kind': 'cat',
		'owner': 'dominic',
		},
	}

for pet, pet_info in pets.items():
	print(pet)
	kinds = pet_info['kind']
	owners = pet_info['owner']
	
	print('\tKind: ' + kinds.title())
	print('\tOwner: ' + owners.title())
