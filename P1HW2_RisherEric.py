# Eric Risher
# 06/19/2024
# P1HW2
# Budget calculator for vacation 

# Questions
print()
print("Going on vacation? Use this planning tool!")
print()
print("What is your budget?:$", end='')
budget_int = float(input())
print("Where is your destination?: ", end='')
destination_string = input()
print("How many miles away is",destination_string,"from where you are?: ", end='')
distances_int = float(input())
print("What is your average miles-per-gallon of gas?: ", end='')
MPG_int = float(input())
print("Average cost of a gallon of gas?: ", end='')
gas_avg = float(input())
print("How much do you have to spend on hotels, parking, and/or passes?: ", end='')
accommodation_int = float(input())
print("How much do you think you will spend for food?: ", end='')
food_int = input()

# Conversions
budget = float(budget_int)
distance = float(distances_int)
MPG = float(MPG_int)
GA = float(gas_avg)
accommodation = float(accommodation_int)
food = float(food_int)

# Calculations
gas = ((distance * 2) / MPG) * GA
expenses = gas + accommodation + food
damage = budget - expenses

# Output
print()
print("------Travel Expenses-----")
print("Location :", destination_string)
print("Starting Budget:$", budget)
print()
print('Fuel Cost: $',gas)
print('Accomodation Cost: $',accommodation)
print('Expected Food Cost: $', food)
print()
print('Remaining Budget: $',damage)
input('Press Enter to get started on your adventure!')
