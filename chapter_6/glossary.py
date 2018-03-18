#6-3 glossary

glossary = {
	'slice':
		'creating a unique list from a parent list',
	'dictionary':
		'creating definitions for values',
	'tuple': 
		'a list of items that cannot change',
	'list':
		'a set of variables that can be modified in different ways',
	'if_statements':
		'a logical tool used to create complex structures within a code',
	'name.title()':
		'creates the given string with a capitalization for the first word',
	'[value].append(whatever)':
		'appends whatever string you want to the parent file indicated by [value]',
	'insert':
		'an insert command can be user to create a given value anywhere within the list',
	'del':
		'the del command permanently deletes anythin from anywhere within the code!',
	'pop':
		'a weird little command which will pop a value out of the list which it is in',		
		}
print("\nA slice is " + glossary['slice'])
print("\nA dictionary is " + glossary['dictionary'])
print("\nA tuple is " + glossary['tuple'])
print("\nA list is " + glossary['list'])
print("\nAn if statement is " + glossary['if_statements'])


for name, definition in glossary.items():
	print("\n" + name.title() + ": " + definition.title())
