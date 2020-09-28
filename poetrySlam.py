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
        print(f'{lines_list.pop(random.randint(0, len(lines_list)-1))}')

#Creation of add line number to line function
def add_line_number(lines_list):
    for i in range(len(lines_list)):
        lines_list[i] = f'{i} {lines_list[i]}'
    return lines_list
        


print(add_line_number(get_file_lines('poem.txt')))
