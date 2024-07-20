# Eric Risher
# 07/17/2024
# Python Final
# This is a grocery shopping program, first we will display grocery items with their prices,
# next our customer gets to input choices, one at a time; After they make their choices,
# we will ask to confirm their done with end. With choices confirmed a list of items is shown
# with a copy of their checkout receipt. Tell the customer how much they owe, ask how much
# cash they plan to use, after tell them how much change will be dispensed, with a total and
# simple form of change.

# Gives change out
def disperse_change(change):
    print('Dispensing...')
    print()
    change = int(change * 100)

    # No change
    if change == 0:
        print("No change")
    # Dollars
    num_dollars = change // 100
    change = change - (num_dollars * 100)
    if num_dollars > 0:
        print(num_dollars, end=' ')
        if num_dollars == 1:
            print("Dollar")
        else:
            print("Dollars")
    # Quarters
    num_quarters = change // 25
    change = change - (num_quarters * 25)
    if num_quarters > 0:
        print(num_quarters, end=' ')
        if num_quarters == 1:
            print("Quarter")
        else:
            print("Quarters")
    # Dimes
    num_dimes = change // 10
    change = change - (num_dimes * 10)
    if num_dimes > 0:
        print(num_dimes, end=' ')
        if num_dimes == 1:
            print("Dime")
        else:
            print("Dimes")
    # Nickles
    num_nickles = change // 5
    change = change - (num_nickles * 5)
    if num_nickles > 0:
        print(num_nickles, end=' ')
        if num_nickles == 1:
            print("Nickle")
        else:
            print("Nickles")
    # Pennies
    num_pennies = change // 1
    if num_pennies > 0:
        print(num_pennies, end=' ')
        if num_pennies == 1:
            print("Penny")
        else:
            print("Pennies")
    print()

# Shows the user which options they have from the stock dictionary.
def show_avail_items(stock):  # Shows what Items are available.
    print('Grocery Item', ' ' * 7, 'Price')
    print('-' * 26)
    for item, price in stock.items(): # For loop, that outputs all items under 20
        print(f'{item:<20} ${stock[item]:.2f}')
    print('-' * 26)


# User is prompted to add items to a cart, which will be represented by a list when done.
def shopping_now(stock):
    bag_area = []
    print('*Welcome to the Grocery Checkout*')
    print()
    while True:
        cart = input("Enter an item to add to the cart or type 'end' to stop adding items: ")
        if cart == 'end':
            break
        elif cart in stock:
            bag_area.append(cart)
        else:
            print("Sorry, we are out of stock of that currently, please make another selection.")
    return bag_area

# Shows which items where chosen from out shopping now function
def show_cart(bag_area):
    print()
    print('The items currently in your cart are:')
    for i in bag_area:
        print(i)

# Checkout receipt
def calc_total(bag_area, stock):
    print('Grocery Checkout Receipt')
    print('-' * 30)
    for i in bag_area:
        if i in stock:
            print(f"{i}                ${stock[i]:.2f}")
    print()
    sub_cost = 0.0
    for i in bag_area:
        if i in stock:
            sub_cost += stock[i]
    print(f"SUBTOTAL:     ${sub_cost:.2f}")
    print()
    tax_amount = sub_cost * 0.02
    print(f'TAX:          ${tax_amount:.2f}')
    post_tot = sub_cost + tax_amount
    print(f'TOTAL:        ${post_tot:.2f}')
    return post_tot

# User putting cash in
def put_cash(post_tot):
    print(f'You owe ${post_tot:.2f} for the groceries')
    print()
    print('How much cash will you put in the self-checkout machine? $', end='')
    use_cash = float(input())
    return use_cash

def change_owed(post_tot, use_cash):
    if post_tot <= use_cash:
        change = use_cash - post_tot
        print(f'The change owed to you is ${change:.2f}')
    return change

def main():
    show_avail_items(stock)
    print()
    bag_area = shopping_now(stock)
    show_cart(bag_area)
    print()
    post_tot = calc_total(bag_area, stock)
    print()
    use_cash = put_cash(post_tot)
    print()
    change = change_owed(post_tot, use_cash)
    print()
    disperse_change(change)
# FUNCTIONFUNCTIONFUNCTIONFUNCTIONFUNCTIONFUNCTIONFUNCTIONFUNCTIONFUNCTIONFUNCTIONFUNCTIONFUNCTION

# DICTIONARY.DICTIONARY.DICTIONARY.DICTIONARY.DICTIONARY.DICTIONARY.DICTIONARY.DICTIONARY.
stock = {
    'apples' : 3.69,
    'berries' : 4.00,
    'chocolate' : 2.89,
    'turkey' : 6.99,
    'cheese' : 4.00,
    'pepsi' : 7.89,
    'eggs' : 3.50,
    'bread' : 3.00

}
# CALLSCALLSCALLSCALLSCALLSCALLSCALLSCALLSCALLSCALLSCALLSCALLSCALLSCALLSCALLSCALLSCALLSCALLSCALLS

main()
input('Enter to exit')