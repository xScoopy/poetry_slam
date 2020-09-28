#Creation of get_file_lines() function
def get_file_lines(filename):
    return open(filename, 'r').readlines()

poem = get_file_lines('poem.txt')
