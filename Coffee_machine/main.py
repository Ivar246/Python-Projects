import time


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}


def is_resource_sufficient(order_ingredients):
    """returns True when order can be made and false when ingredients are not sufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f'sorry, there is not enough {item}..')
            return False
    return True


def is_transaction_sucessful(amount_received, drink_cost):
    """return true when payment is accepted or false if money is insufficient"""
    if amount_received > drink_cost:
        change = round(amount_received - drink_cost, 2)
        print('processing ...')
        time.sleep(2)
        print(f'\nhere is ${change} in change')
        global profit
        profit += drink_cost
        return True
    else:
        print('sorry, insufficient money, money refunded.')
        
    
def process_coin():
    """return the total calculation from the coin inserted"""
    print("Please insert coin..")
    total = int(input('How many quarters?: '))*0.25
    total += int(input('How many dimes?: '))*0.1
    total += int(input('How many pennies?: '))*0.01
    total += int(input('How many nickels?: '))*0.05
    
    return total 


def make_coffee(drink_name, order_ingredients):
    """deduct the required ingredients from resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f'Here is your {drink_name}☕')    
          
is_on = True
while is_on:
    choice = input('What is your choice? (espresso/latte/cappuccino): ').lower()
    if choice =='off':
        is_on = False
    elif choice == 'report':
        for item in resources:
            print(f"{item} : {resources[item]}")   
        print(f'money: {profit}')
    else:
        drink = MENU[choice]   
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coin()  
            if is_transaction_sucessful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])      
                