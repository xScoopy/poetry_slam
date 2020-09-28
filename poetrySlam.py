#Creation of get_file_lines() function
def get_file_lines(filename):
    return open(filename, 'r').read().strip().split('\n')

#Creation of lines_printed_backwards() function
def lines_printed_backwards(lines_list):
    for i in range(len(lines_list)- 1, -1, -1):
        print(f'{i + 1} {lines_list[i]}')
        
        

lines_printed_backwards(get_file_lines('poem.txt'))
