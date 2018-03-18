# 8-11 Unchanged magicians: make the functions call upon a copy so that the original list is unchanged and show that you have one list of the original names and one list with 'the Great' added to each magus name.

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

show_magicians(unprinted_magus[:])
make_great(printed_magus)
