# Eric Risher
# 07/11/2024
# P4 Lab 2
# This program will display a multiplication table

# use while to control the program

keep_going = 'yes'

while keep_going.lower() == 'yes':
    # for loop goes here
    num = int(input('Enter an integer: '))
    print('\n')
    
    if num >= 0:
        for i in range(1, 12 +1):
            print(f'{num} * {i} = {num * i}')
        print('\n')
    else:
        print('This program does not handle negative numbers')
        print('\n')
        
    # Safe Guard
    keep_going = input('Would you like to run the program again? Enter yes or no: ')

# Input for Exit
input('Press Enter to Exit program')
