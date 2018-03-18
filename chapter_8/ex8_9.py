# 8-9 Magicians: Make a list of magicians names. Pass the list to a function
# which prints the name of each magician in the list

def show_magicians(unprinted_magus):

    while unprinted_magus:
        magus = unprinted_magus.pop()
        print(f'the magus ' + magus.title())
        printed_magus.append(magus)

unprinted_magus = ['hodini', 'jacob', 'theodore']
printed_magus = []

show_magicians(unprinted_magus)
