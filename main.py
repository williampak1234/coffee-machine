class CoffeeMachine:
    def __init__(self, water=400, milk=540, beans=120, cups=9, money=550):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    def print_main_menu(self):
        print("Write action (buy, fill, take, remaining, exit):")
        user_menu_choice = input()
        self.do_users_action(user_menu_choice)

    def print_buy_menu(self):
        return input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")

    def do_users_action(self, users_choice):
        if users_choice == "buy":
            self.buy()
        elif users_choice == "fill":
            self.fill()
        elif users_choice == "take":
            self.take()
        elif users_choice == "remaining":
            print(self.remaining())
        elif users_choice == "exit":
            exit()

    def buy(self):
        buyers_choice = self.print_buy_menu()
        if buyers_choice == "back":
            return

        qualifications = self.can_buy(buyers_choice)

        if buyers_choice == "1":
            if qualifications[0]:
                self.buy_espresso()
            else:
                print(f"Sorry, not enough {qualifications[1]}")

        elif buyers_choice == "2":
            if qualifications[0]:
                self.buy_latte()
            else:
                print(f"Sorry, not enough {qualifications[1]}")

        elif buyers_choice == "3":
            if qualifications[0]:
                self.buy_cappuccino()
            else:
                print(f"Sorry, not enough {qualifications[1]}")

    def buy_espresso(self):
        print("I have enough resources, making you a coffee!")
        self.water -= 250
        self.beans -= 16
        self.cups -= 1
        self.money += 4

    def buy_latte(self):
        print("I have enough resources, making you a coffee!")
        self.water -= 350
        self.milk -= 75
        self.beans -= 20
        self.cups -= 1
        self.money += 7

    def buy_cappuccino(self):
        print("I have enough resources, making you a coffee!")
        self.water -= 200
        self.milk -= 100
        self.beans -= 12
        self.cups -= 1
        self.money += 6

    def can_buy(self, menu_choice):
        materials_required = {
            "1" : {
                "water" : 250,
                "milk" : 0,
                "beans" : 16
                },

            "2" : {
                "water" : 350,
                "milk" : 75,
                "beans" : 20
                },

            "3" : {
                "water" : 200,
                "milk" : 100,
                "beans" : 12
                },
        }

        existing_materials = {
            "water" : self.water,
            "milk" : self.milk,
            "beans" : self.beans
        }

        for materials in materials_required[menu_choice]:
            if materials_required[menu_choice][materials] > existing_materials[materials]:
                return False, materials

        return True, None

    def fill(self):
        print("Write how many ml of water you want to add:")
        self.water += int(input())

        print("Write how many ml of milk you want to add:")
        self.milk += int(input())

        print("Write how many grams of coffee beans you want to add:")
        self.beans += int(input())

        print("Write how many disposable cups you want to add:")
        self.cups += int(input())

    def take(self):
        print(f"I gave you ${self.money}")
        self.money -= self.money

    def remaining(self):
        return f"""
The coffee machine has: 
{self.water} ml of water
{self.milk} ml of milk
{self.beans} g of coffee beans
{self.cups} disposable cups
${self.money} of money
"""

wawa = CoffeeMachine()

if __name__ == "__main__":
    while True:
        wawa.print_main_menu()

