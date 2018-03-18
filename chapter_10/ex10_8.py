filename1 = 'cats.txt'
filename2 = 'dogs.txt'

try:
    with open(filename1) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    pass
else:
    # Read what is inside of the file.
    words = contents.split()
    print(words)

try:
    with open(filename2) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    pass
else:
    # Read what is inside of the file.
    words = contents.split()
    print(words)
