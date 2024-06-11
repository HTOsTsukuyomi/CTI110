# Eric Risher
# 06/11/2024
# P1LAB1
# We need to have the user input their first and last names, then be greeted.(We use the .format to allow the "!")
print('Enter your First name:', end='')
firstname = input()
print('Enter your last name:', end='')
lastname = input()
print('Hello, {} {}! Welcome to CTI-110.'.format(firstname, lastname))