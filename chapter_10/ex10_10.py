def count_words(filename):
    """Count the approximate number of words in a file"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        # Count the approzimate number of times a chosen word is in the file.
        words = contents.split()
        num_words = words.count('the')
        print("The file " + filename + " has 'the' " + str(num_words) +
        " times in the file")

filenames = ['alice.txt']
for filename in filenames:
    count_words(filename)
