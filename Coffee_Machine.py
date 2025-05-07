import Menu
import Art
is_on = True
dispense_coffee = True

starting_water = Menu.resources["water"]
starting_beans = Menu.resources["coffee"]
starting_milk = Menu.resources["milk"]
profit = 0
# Change the remaining amounts
remaining_water = starting_water
remaining_milk = starting_milk
remaining_coffee = starting_beans
new_profit = profit

def sum_money():
    '''Totals the money entered into the coffee machine'''
    coin_500_tv = coin_500 * 500
    coin_100_tv = coin_100 * 100
    coin_50_tv = coin_50 * 50
    coin_10_tv = coin_10 * 10
    money_entered = coin_500_tv + coin_100_tv + coin_50_tv + coin_10_tv
    return money_entered

def money_check(money_entered):
    '''Checks if there is enough money in the machine '''
    global dispense_coffee, new_profit
    if money_entered >= coffee_cost:
        otsuri = money_entered - coffee_cost
        new_profit  += coffee_cost
        print(f"Your change is {otsuri} yen.")
        dispense_coffee = True
    else:
        print("Sorry that's not enough money. Money refunded, please put in more coins.")
        dispense_coffee= False
    return dispense_coffee, new_profit

def subtract_ingredients(water, milk, coffee):
    '''Subtract ingredients used from the remaining ingredients'''
    global dispense_coffee, remaining_coffee, remaining_water, remaining_milk
    remaining_water -= coffee_water
    remaining_milk -= coffee_milk
    remaining_coffee -= coffee_beans
    if remaining_coffee < 0:
        dispense_coffee = False
        print(f"Sorry there is not enough coffee.")
    elif remaining_milk < 0:
        dispense_coffee = False
        print(f"Sorry there is not enough milk")
    elif remaining_water < 0:
        dispense_coffee = False
        print(f"Sorry there is not enough water")
    else:
        print(f"Here is your {coffee_selection}")
        print(Art.coffee)
    return remaining_milk, remaining_coffee, remaining_water, dispense_coffee

while dispense_coffee and is_on:
    coffee_selection = input("What would you like. Please choose espresso, latte, or cappuccino: ").lower()
    if coffee_selection == "off":
        is_on = False
    elif coffee_selection == "report":
        print(f"Water: {remaining_water}mL")
        print(f"Milk: {remaining_milk}mL")
        print(f"Coffee: {remaining_coffee}g")
        print(f"Money: {new_profit} yen")
        dispense_coffee = False
    else:
        coffee_cost = Menu.MENU[coffee_selection]["cost"]
        coffee_water = Menu.MENU[coffee_selection]["ingredients"]["water"]
        coffee_beans = Menu.MENU[coffee_selection]["ingredients"]["coffee"]
        if coffee_selection == "espresso":
            coffee_milk = 0
        else:
            coffee_milk = Menu.MENU[coffee_selection]["ingredients"]["milk"]

        coin_500 = int(input("How many 500 yen coins? "))
        coin_100 = int(input("How many 100 yen coins? "))
        coin_50 = int(input("How many 50 yen coins? "))
        coin_10 = int(input("How many 10 yen coins? "))
        subtract_ingredients(water=remaining_water, milk=remaining_milk, coffee=remaining_coffee)
        if not dispense_coffee:
            break
        money_entered = sum_money()
        dispense_coffee = money_check(money_entered)
