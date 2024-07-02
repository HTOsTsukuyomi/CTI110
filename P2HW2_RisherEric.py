# Eric Risher
# 6/26/2024
# P2 HomeWork 2
# This python script takes 6 grades from Module tests,
# stores those variables in a list, then gives calculations.

# First, we need to ask the user for 6 module grades on separate lines.

print('Enter grade for Module 1: ', end='')    # Module 1
string_module1 = input()

print('Enter grade for Module 2: ', end='')    # Module 2
string_module2 = input()

print('Enter grade for Module 3: ', end='')    # Module 3
string_module3 = input()

print('Enter grade for Module 4: ', end='')    # Module 4
string_module4 = input()

print('Enter grade for Module 5: ', end='')    # Module 5
string_module5 = input()

print('Enter grade for Module 6: ', end='')    # Module 6
string_module6 = input()

print()     # Blank space

# Before we store our values, lets convert them from string to float, ya' know to be safe and stuff.
module1 = float(string_module1)
module2 = float(string_module2)
module3 = float(string_module3)
module4 = float(string_module4)
module5 = float(string_module5)
module6 = float(string_module6)

# Next, we need to store each of those Modules into a list with a descriptive name.
semester_grades = [module1, module2, module3, module4, module5, module6]    # List

# Calculating average
average = sum(semester_grades) / len(semester_grades)

# After that, display the lowest,highest,sum, and grade average. Must be beautified.
print('---------------Results---------------')                # Title
print(f'Lowest Grade:          {min(semester_grades)}')       # lowest
print(f'Highest Grade:         {max(semester_grades)}')       # highest
print(f'Sum of Grades:         {sum(semester_grades)}')       # sum
print(f'Average:               {average:.2f}')                # average
print('---------------------------------------------')        # Ending

# Finally, allow the user to take note of info, then exit.
print()
print()
input('Press Enter to Exit')