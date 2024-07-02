# Eric Risher
# 6/26/2024
# P2 HomeWork 1
# A python script that will help us to calculate,
# and display our travel expenses, neatly.

# We need to tell our user what our script is for.
print('This program calculates and displays travel expenses')
print()

# Let them input their budget in a value for the USD.
print('Enter Budget: ', end='')
string_budget = input()
print()

# Ask the user, where they will be going?
print('Enter your travel destination: ', end='')
string_destination = input()
print()

# Ask their expected gas expenses.
print('How much do you think you will spend on gas? ', end='')
string_gas = input()
print()

# A rough estimate of how much accommodation / hotel will be.
print('Approximately, how much will you need for accomodation/hotel? ', end='')
string_AH = input()
print()

# Last question, how much for food?
print('Last, how much do you need for food? ', end='')
string_food = input()
print()

# Convert string inputs into correct forms.
budget = float(string_budget)
destination = string_destination
gas = float(string_gas)
ah = float(string_AH)
food = float(string_food)

# Run calculations.
rb = budget - (gas + ah + food)

# Output a beautified travel expense report
print("------------Travel Expenses------------")
print(f'Location:           {destination}')
print(f'Initial Budget:     ${budget:.2f}')
print(f'Fuel:               ${gas:.2f}')
print(f'Accomodation:       ${ah:.2f}')
print(f'Food:               ${food:.2f}')
print('---------------------------------------')
# Output a beautified verison of their remaining balance.
print()
print(f'Remaining Balance:  ${rb:.2f}')
# Let the use take down info, then let them hit 'Enter' to exit.
print()
print()
input('Press Enter When Ready to Exit')
