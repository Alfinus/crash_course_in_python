# 6-5 Rivers

rivers = {'nile': 'egypt', 'mississippi': 'usa', 'amazon': 'brazil',}

for river, country in rivers.items():
	print("\nThe " + river.title() + " is in " + country.title() + ".")
print("\nA list of Rivers found in this dictionary: ")
for river in rivers.keys():
	print(river.title())
print("\nA list of countrys found in this dictionary: ")
for country in rivers.values():
	print(country.title())
