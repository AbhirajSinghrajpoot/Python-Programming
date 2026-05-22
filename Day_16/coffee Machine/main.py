from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ").strip().lower()

    if choice == "off":
        is_on = False
    elif choice == "report":
        print(coffee_maker.report())
        print(money_machine.report())
    else:
        drink = menu.find_drink(choice)
        if drink:
            print(f"{drink.name.title()} costs Rs. {drink.cost}")
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    print(coffee_maker.make_coffee(drink))
        else:
            print("Sorry, that drink is not available.")