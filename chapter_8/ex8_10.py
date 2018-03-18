# 8-10 'great'  Magicians: write a function which modifies the list of magicians by adding 'the Great' to each name.

def show_magicians(unprinted_magus):

    while unprinted_magus:
        magus = unprinted_magus.pop()
        print(magus.title())
        printed_magus.append(magus)

def make_great(printed_magus):
        while printed_magus:
            great = printed_magus.pop()
            print('the Great ' + great.title())
            great_magus.append(great)

unprinted_magus = ['hodini', 'jacob', 'theodore']
printed_magus = []
great_magus = []

show_magicians(unprinted_magus)
make_great(printed_magus)
