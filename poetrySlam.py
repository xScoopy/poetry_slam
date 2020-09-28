import random
#Creation of get_file_lines() function
def get_file_lines(filename):
    return open(filename, 'r').read().strip().split('\n')

#Creation of lines_printed_backwards() function
def lines_printed_backwards(lines_list):
    for i in range(len(lines_list)- 1, -1, -1):
        print(f'{i + 1} {lines_list[i]}')

#Creation of lines_printed_random() function
def lines_printed_random(lines_list):
    while len(lines_list) > 0: 
        
        #for i in range(len(lines_list)):
        print(f'{lines_list.pop(random.randint(0, len(lines_list)-1))}')
        
#Creation of add line number to line function



lines_printed_random(get_file_lines('poem.txt'))
