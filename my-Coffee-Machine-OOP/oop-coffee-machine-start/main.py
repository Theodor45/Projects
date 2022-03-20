from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from os import system 
import time
import pyperclip
import signal
import sys

print("Welcome to the Coffee-Machine!")
print("Press Ctrl-C to quit.")

# Catch Keyboard Interrupt
def sigint_handler(signal, frame):
    print ('Bye!')
    sys.exit(0)
signal.signal(signal.SIGINT, sigint_handler)

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
end_of_game = False

# Clears teminal for linux (my os)
def clear():
    system('clear')

while not end_of_game:
    choice = str(input("What would you like? (espresso/latte/cappuccino): ")).lower()
    # Getting the machine to quit
    if choice == 'off':
        quit()
    # Get machine to write a report on resources
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        # Checking if coffee exists
        if menu.find_drink(choice) is None:
            print("Enter a valid choice!")
            sys.exit(0)
        else:
            drink = menu.find_drink(choice)
        # Checking if resource sufficient
        if coffee_maker.is_resource_sufficient(drink) == True:
            pass
        else:
            print(f"Sorry we don't have enough resources for {choice}")
            sys.exit(0)
        # Checking for money
        cost = drink.cost
        if money_machine.make_payment(cost) == False:
            print("Sorry, you don't have enough money!")
            sys.exit(0)
        else:
            pass
        coffee_maker.make_coffee(drink)
        pyperclip.copy('##$/ Tranzaction completed! /$##')
        pyperclip.paste()
        time.sleep(4)
        clear()