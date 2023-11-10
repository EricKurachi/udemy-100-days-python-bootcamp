MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

COINS = {
    "quarter": 0.25,
    "dime": 0.10,
    "nickle": 0.05,
    "pennie": 0.01,
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def show_report(money):
    water_quantity = resources["water"]
    milk_quantity = resources["milk"]
    coffee_quantity = resources["coffee"]

    print(f"Water: {water_quantity}ml")
    print(f"Milk: {milk_quantity}ml")
    print(f"Coffee: {coffee_quantity}g")
    print(f"Money: ${money}")


def resources_check(drink):
    """Checks if there are enough resources to make specified drink.
    Returns True if resources are available and False if there are not enough resources"""
    ingredients_required = MENU[drink]["ingredients"]
    for ingredient in ingredients_required:
        if ingredients_required[ingredient] > resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient}")
            return False
    return True


def process_coins():
    total_money = 0
    print("Please insert coins.")
    for coin in COINS:
        coins_inserted = int(input(f"how many {coin}s?: "))
        total_money += coins_inserted * COINS[coin]
    return round(total_money, 2)


def check_transaction(drink, payment):
    drink_cost = MENU[drink]["cost"]
    change = payment - drink_cost
    if change < 0:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        print(f"Here is ${change} in change.")
        return change


def make_coffee(drink_choice):
    ingredients = MENU[drink_choice]["ingredients"]
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]
    print(f"Here is your {choice} ☕. Enjoy!")


is_on = True
money_stored = 0

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")

    if choice == "report":
        show_report(money_stored)

    elif choice == "off":
        is_on = False

    else:
        enough_resources = resources_check(choice)
        if enough_resources:
            money_received = process_coins()
            change_to_give = check_transaction(choice, money_received)
            if change_to_give is not False:
                money_stored += MENU[choice]["cost"]
                make_coffee(choice)
