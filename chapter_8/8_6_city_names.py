#8-6 City names: Write a function that takes in the name of a city
# and its country. The function should return a string.

def city_country(city, country):
	'''Takes in the name of a city and its country'''
	city_country = city + ',' + country
	return city_country.title()
	
seattle = city_country('seattle', 'usa') 
print ('\n' + seattle)

san_fran = city_country('san fransisco', 'usa')
print('\n' + san_fran)

berlin = city_country('berlin', 'germany')
print('\n' + berlin)
