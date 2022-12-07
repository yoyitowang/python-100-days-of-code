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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def print_report():
    global resources, money
    for resource, remain in resources.items():
        unit = 'g' if resource == 'coffee' else 'ml'
        print(f'{resource}: {remain}{unit}')
    print(f'Money: ${money}')

def check_resources(drink):
    ingredients = MENU[drink]['ingredients']
    enough = True
    for ingredient, cost in ingredients.items():
        if resources[ingredient] < cost:
            print(f'Sorry there is not enough {ingredient}')
            enough = False
    return enough

def insert_coins():
    print('Please insert coins:')
    quarters = int(input('- quarters: '))
    dimes = int(input('- dimes: '))
    nickles = int(input('- nickles: '))
    pennies = int(input('- pennies: '))
    total = quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01
    return total

def check_transaction(total, drink):
    if total - MENU[drink]['cost'] < 0:
        print("Sorry that's not enough money. Money refunded.")
        return False
    return True

    
def make_coffee(drink, paid):
    global resources
    for ingredient, cost in MENU[drink]['ingredients'].items():
        resources[ingredient] -= cost
    m = paid-MENU[drink]['cost']
    print(f'Here is ${m} dollars in change\n')

    print_report()
    print(f'Here is your {drink}, Enjoy!')


    

if __name__ == '__main__':
    work = True
    money = 0
    while work:
        user = input('What do you like? (espresso/latte/cappuccino):').lower()
        if user == 'off':
            print('Thanks!')
            break
        elif user == 'report':
            print_report()
        elif user in MENU.keys():
            if check_resources(user):
                paid = insert_coins()
                if check_transaction(paid, user):
                    money += MENU[user]['cost']
                    make_coffee(user, paid)
                    
                                    