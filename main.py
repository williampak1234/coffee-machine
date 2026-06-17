water_amount = 400
milk_amount = 540
bean_amount = 120
cups_amount = 9
money_amount = 550


def show_stats():
    print(f"""The coffee machine has: 
{water_amount} ml of water
{milk_amount} ml of milk 
{bean_amount} g of coffee beans
{cups_amount} disposable cups
${money_amount} of money
""")

def get_choice():
    print("Write action (buy, fill, take): ")
    action = input()
    return action

def do_action():
    show_stats()

    user_choice = get_choice()
    if user_choice == "buy":
        new_stats = buy(water_amount, milk_amount, bean_amount, cups_amount, money_amount)
        return new_stats
    elif user_choice == "fill":
        new_stats = fill(water_amount, milk_amount, bean_amount, cups_amount, money_amount)
        return new_stats
    else:
        new_stats = take(water_amount, milk_amount, bean_amount, cups_amount, money_amount)
        return new_stats

def buy(water=water_amount, milk=milk_amount, bean=bean_amount, cups=cups_amount, money=money_amount):
    what_bought = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: "))
    if what_bought == 1:
        water -= 250
        bean -= 16
        cups -= 1
        money += 4
    elif what_bought == 2:
        water -= 350
        milk -= 75
        bean -= 20
        cups -= 1
        money += 7
    else:
        water -= 200
        milk -= 100
        bean -= 12
        cups -= 1
        money += 6
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


updated_stats = do_action()

water_amount = updated_stats[0]
milk_amount = updated_stats[1]
bean_amount = updated_stats[2]
cups_amount = updated_stats[3]
money_amount = updated_stats[4]

show_stats()
exit()