#importing random and os for functions and clearing the screen
import random
import os 
#Creation of get_file_lines() function
def get_file_lines(filename):
    return open(filename, 'r').read().strip().split('\n')

#Creation of lines_printed_normally() function
def lines_printed_normally(lines_list):
    for i in range(len(lines_list)):
        print(f'{lines_list[i]}')

#Creation of lines_printed_backwards() function
def lines_printed_backwards(lines_list):
    for i in range(len(lines_list)- 1, -1, -1):
        print(f'{lines_list[i]}')

#Creation of lines_printed_random() function
#Function uses while loop to grab a random int to use for the index, pops the index to avoid having any repeat lines
def lines_printed_random(lines_list):
    while len(lines_list) > 0: 
        print(f'{lines_list.pop(random.randint(0, len(lines_list)-1))}')

#Creation of add line number to line function
#This is used to print the original poem line number to ensure no repeat lines are used in my random print function. 
def add_line_number(lines_list):
    for i in range(len(lines_list)):
        lines_list[i] = f'{i + 1} {lines_list[i]}'
    return lines_list

#Creation of lines_printed_custom() function
#this function sorts the lines by length, then will print out based on the first parameter either shortest to longest, or vice versa
def lines_printed_custom(length, lines_list):
    lines_list.sort(key = len)
    if length.upper() == 'SHORT':
        for i in range(len(lines_list)):
            print(lines_list[i])
    if length.upper() == 'LONG' :
        lines_printed_backwards(lines_list)

#Function to print out the menu of options to choose from
def get_user_input():
    print("1. Display the poem as it was written.")
    print("2. Display the poem written backwards.")
    print("3. Display the poem in a randomly written order.")
    print("4. Display the poem lines from shortest to longest.")
    print("5. Display the poem lines from longest to shortest.\n")
    return input("Please choose a number, or type 'done' to exit the poetry slam\n")
    


#Below are the functions used to test each one as it was built:

#print(add_line_number(get_file_lines('poem.txt')))
#lines_printed_backwards(add_line_number(get_file_lines('poem.txt')))
#lines_printed_random(add_line_number(get_file_lines('poem.txt')))
#lines_printed_custom('long', get_file_lines('poem.txt'))
#lines_printed_normally(add_line_number(get_file_lines('poem.txt')))

#Welcome statements
print("Welcome to my poetry Slam!")
print("Today we are featuring 'Mother to Son' by Langston Hughes")
print("Please make a selection below:\n")

#While loop to continuously loop through choices until the user types 'done'
#line breaks and input() added to visually clean up the user experience
while True:
    choice = get_user_input()
    if choice == '1':
        print('\n')
        lines_printed_normally(add_line_number(get_file_lines('poem.txt')))
        print('\n')
        input("press Enter to continue...")
        os.system('clear')
    elif choice == '2':
        print('\n')
        lines_printed_backwards(add_line_number(get_file_lines('poem.txt')))
        print('\n')
        input("press Enter to continue...")
        os.system('clear')
    elif choice == '3':
        print('\n')
        lines_printed_random(add_line_number(get_file_lines('poem.txt')))
        print('\n')
        input("press Enter to continue...")
        os.system('clear')
    elif choice == '4':
        print('\n')
        lines_printed_custom('short', get_file_lines('poem.txt'))
        print('\n')
        input("press Enter to continue...")
        os.system('clear')
    elif choice == '5':
        print('\n')
        lines_printed_custom('long', get_file_lines('poem.txt'))
        print('\n')
        input("press Enter to continue...")
        os.system('clear')
    elif choice.upper() == 'DONE':
        break
    else:
        print('\n')
        print("Please make a valid selection choosing a number 1 through 5 or 'done' to exit")
        input("Press Enter to return to the menu")
        os.system('clear')



