favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

print("Sarah's favorite language is " +
	favorite_languages['sarah'].title() +
	".")
	
for n, l in favorite_languages.items():
	print(n.title() + "'s favorite language is " + l.title() + ".")


for name in favorite_languages.keys():
	print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(name.title())
	
	if name in friends:
		print(" Hi " + name.title() +
			", I see you favorite language is " +
			favorite_languages[name].title() + "!")

if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll!")

for name in sorted(favorite_languages.keys()):
	print(name.title() + ", thank you for taking the poll.")

print("The following languages have been mentioned:")
for language in favorite_languages.values():
	print(language.title())

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
	print(language.title())
