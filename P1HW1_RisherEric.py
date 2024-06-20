# Eric Risher
# 06/18/2024
# P1HW1
# Calculating Exponents & Addition and Subtraction

print('-----Calculating Exponenets----')
#breath
print()

# First we need our base and exponent values
print("Enter an interger as the base value: ", end='')
base_string = input()

print("Enter an interger as the exponent: ", end='')
exponent_string = input()

# Next convert those strings into integers ('string' ** 'string' will give us an error)
base = int(base_string)
exponent = int(exponent_string)

# Now we have integers, we can calculate them with our next line
total1 = base ** exponent

# Breath
print()

#proof
print(base, 'raised to the power of', exponent, 'is', total1, '!!')

# Breath
print()

# Next task
print("-----Addition and Subtraction----")

# Breath
print()

# Finally we need our X Y Z values
print("Enter a starting integer: ", end='')
X_string = input()

print("Enter an integer to add: ", end='')
Y_string = input()

print("Enter an integer to subtract: ", end='')
Z_string = input()

# String to Integer
x = int(X_string)
y = int(Y_string)
z = int(Z_string)

# Calculations
total2 = x + y - z

# Breath
print()

#proof two
print(x, '+', y, '-', z, 'is equal to',total2)

#breath
print()

# Let the user see their totals by halting until there is input
input("Hit Enter to clean up...")