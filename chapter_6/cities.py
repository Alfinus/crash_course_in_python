# cities... looking for the name of a song, the country its in, general
#population, and a fun fact about that city.

cities = {
	'seattle': {
		'country': 'usa',
		'population': '3,798,902',
		'fun_fact': 'Seattle is the birthplace of Starbucks, the world’s largest coffee chain.',
			},
	'berlin': {
		'country': 'germany',
		'population': "3,593,000",
		'fun_fact': 'Berlin has more bridges than Venice',
			},
	'chicago': {
		'country': 'usa',
		'population': '2,704,958',
		'fun_fact': 'chicago is the third largest city in the us',
			},
		}
		
for city, city_info in cities.items():
	print(city)
	country = city_info['country']
	population = city_info['population']
	fun_fact = city_info['fun_fact']
	
	print('\tCountry: ' + country.title())
	print('\tPopulation: ' + population.title())
	print('\tFun fact!: ' + fun_fact.title())
