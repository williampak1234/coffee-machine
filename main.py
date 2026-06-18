water_amount = 400
milk_amount = 540
bean_amount = 120
cups_amount = 9
money_amount = 550

running = True


def show_stats(water, milk, bean, cup, money):

    print(f"""The coffee machine has: 
{water} ml of water
{milk} ml of milk 
{bean} g of coffee beans
{cup} disposable cups
${money} of money
""")

def main_menu():
    print("Write action (buy, fill, take, remaining, exit): ")
    action = input()
    return action

def do_action(user_input):
    user_choice = user_input

    if user_choice == "buy":
        new_stats = buy(water_amount, milk_amount, bean_amount, cups_amount, money_amount)
        return new_stats

    elif user_choice == "fill":
        new_stats = fill(water_amount, milk_amount, bean_amount, cups_amount, money_amount)
        return new_stats

    elif user_choice == "take":
        new_stats = take(water_amount, milk_amount, bean_amount, cups_amount, money_amount)
        return new_stats

    elif user_choice == "remaining":
        show_stats(water_amount, milk_amount, bean_amount, cups_amount, money_amount)

    elif user_choice == "exit":
        exit()

    return water_amount, milk_amount, bean_amount, cups_amount, money_amount

def can_buy(user_menu_choice, water_left, milk_left, bean_left, cups_left):
    user_menu_choice = int(user_menu_choice)
    # Error message for when user wants to buy an espresso, but the machine doesn't have enough materials.
    if user_menu_choice == 1:
        if water_left < 250:
            print(f"Sorry, not enough water!")
            return False
        elif bean_left < 16:
            print(f"Sorry, not enough beans!")
            return False
        elif cups_left < 1:
            print("Sorry, not enough cups!")
            return False

    # Error message for when user wants to buy a latte, but the machine doesn't have enough materials.
    elif user_menu_choice == 2:
        if water_left < 350:
            print(f"Sorry, not enough water!")
            return False
        elif milk_left < 75:
            print("Sorry, not enough milk!")
            return False
        elif bean_left < 20:
            print(f"Sorry, not enough beans!")
            return False
        elif cups_left < 1:
            print("Sorry, not enough cups!")
            return False


    # Error message for when user wants to buy a cappuccino but the machine doesn't have enough materials.
    elif user_menu_choice == 3:
        if water_left < 200:
            print(f"Sorry, not enough water!")
            return False
        elif milk_left < 100:
            print("Sorry, not enough milk!")
            return False
        elif bean_left < 12:
            print(f"Sorry, not enough beans!")
            return False
        elif cups_left < 1:
            print("Sorry, not enough cups!")
            return False


    return True

def buy(water=water_amount, milk=milk_amount, bean=bean_amount, cups=cups_amount, money=money_amount):
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:, back - to main menu:")
    what_bought = input()

    if what_bought == "back":
        return water_amount, milk_amount, bean_amount, cups_amount, money_amount

    # Verification step
    has_enough = can_buy(what_bought, water, milk, bean, cups)
    if has_enough:
        pass
    elif not has_enough:
        return water, milk, bean, cups, money

    if what_bought == '1':
        water -= 250
        bean -= 16
        cups -= 1
        money += 4
    elif what_bought == '2':
        water -= 350
        milk -= 75
        bean -= 20
        cups -= 1
        money += 7
    elif what_bought == '3':
        water -= 200
        milk -= 100
        bean -= 12
        cups -= 1
        money += 6

    print("I have enough resources, making you a coffee!")
    return water, milk, bean, cups, money

def fill(water=water_amount, milk=milk_amount, bean=bean_amount, cups=cups_amount, money=money_amount):
    print("Write how many ml of water you want to add: ")
    add_water = int(input())

    print("Write how many ml of milk you want to add: ")
    add_milk = int(input())

    print("Write how many grams of coffee beans you want to add: ")
    add_beans = int(input())

    print("Write how many disposable cups you want to add: ")
    add_cups = int(input())

    water += add_water
    milk += add_milk
    bean += add_beans
    cups += add_cups

    return water, milk, bean, cups, money

def take(water=water_amount, milk=milk_amount, bean=bean_amount, cups=cups_amount, money=money_amount):
    print(f"I gave you ${money}")
    money = 0
    return water, milk, bean, cups, money


while running:
    user_decision = main_menu()  # Get user Decision from the main menu
    coffee_machine_stock = do_action(user_decision)  # Executes that decision, and returns the new stock as a tuple

    # Updates the stats of the coffee machine for every run of the loop
    water_amount = coffee_machine_stock[0]
    milk_amount = coffee_machine_stock[1]
    bean_amount = coffee_machine_stock[2]
    cups_amount = coffee_machine_stock[3]
    money_amount = coffee_machine_stock[4]


