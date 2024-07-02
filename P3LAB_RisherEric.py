# Eric Risher
# 07/02/2024
# P3LAB
# Python script that allows the user to input their own,
# money value and then give change based on the input.

# Get float
print('Enter the amount of money as a float: $', end='')
money_tot = float(input())

# Convert
money_tot = int(money_tot * 100)

# No change
if money_tot == 0:
    print("No change")

# Dollars
num_dollars = money_tot // 100
money_tot = money_tot - (num_dollars * 100)

if num_dollars > 0:
    print(num_dollars, end=' ')
    if num_dollars == 1:
        print("Dollar")
    else:
        print("Dollars")

# Quarters
num_quarters = money_tot // 25
money_tot = money_tot - (num_quarters * 25)

if num_quarters > 0:
    print(num_quarters, end=' ')
    if num_quarters == 1:
        print("Quarter")
    else:
        print("Quarters")

# Dimes
num_dimes = money_tot // 10
money_tot = money_tot - (num_dimes * 10)

if num_dimes > 0:
    print(num_dimes, end=' ')
    if num_dimes == 1:
        print("Dime")
    else:
        print("Dimes")

# Nickles
num_nickles = money_tot // 5
money_tot = money_tot - (num_nickles * 5)

if num_nickles > 0:
    print(num_nickles, end=' ')
    if num_nickles == 1:
        print("Nickle")
    else:
        print("Nickles")

# Pennies
num_pennies = money_tot // 1

if num_pennies > 0:
    print(num_pennies, end=' ')
    if num_pennies == 1:
        print("Penny")
    else:
        print("Pennies")

print()
input('Enter to Exit')