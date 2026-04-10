def show_current_state(current_water: int, current_milk: int, current_coffee_beans: int, current_disposable_cups: int, current_money: int) -> None:
    """Print the current state of the coffee machine

    :param current_water: the current water in the machine.
    :param current_milk: the current milk in the machine.
    :param current_coffee_beans: the current coffee beans in the machine.
    :param current_disposable_cups: the current disposable cups in the machine.
    :param current_money: the current money in the machine.
    """
    print()
    print("The coffee machine has:")
    print(f"{current_water} ml of water")
    print(f"{current_milk} ml of milk")
    print(f"{current_coffee_beans} g of coffee beans")
    print(f"{current_disposable_cups} disposable cups")
    print(f"${current_money} of money")


def get_action(user_input: str, current_water: int, current_milk: int, current_coffee_beans: int, current_disposable_cups: int, current_money: int) -> tuple :
    """Take input from the user and select the action to take according to it

    :param user_input: the input from the user
    :param current_water: the current water in the machine.
    :param current_milk: the current milk in the machine.
    :param current_coffee_beans: the current coffee beans in the machine.
    :param current_disposable_cups: the current disposable cups in the machine.
    :param current_money: the current money in the machine.
    :return: a tuple of the current water, current milk, current coffee beans, current disposable cups and current money
    """
    match user_input:
        case "buy":
            return buy_action(current_water, current_milk, current_coffee_beans, current_disposable_cups, current_money)
        case "fill":
            return fill_action(current_water, current_milk, current_coffee_beans, current_disposable_cups, current_money)
        case "take":
            return current_water, current_milk, current_coffee_beans, current_disposable_cups, take_action(current_money)
        case "remaining":
            show_current_state(current_water, current_milk, current_coffee_beans, current_disposable_cups, current_money)
            return current_water, current_milk, current_coffee_beans, current_disposable_cups, current_money
        case _:
            print("Invalid action")
            return current_water, current_milk, current_coffee_beans, current_disposable_cups, current_money



def buy_action(current_water: int, current_milk: int, current_coffee_beans: int, current_disposable_cups: int, current_money: int) -> tuple :
    """Handle the type of coffee that will be bought from the machine.

    :param current_water: the current water in the machine.
    :param current_milk: the current milk in the machine.
    :param current_coffee_beans: the current coffee beans in the machine.
    :param current_disposable_cups: the current disposable cups in the machine.
    :param current_money: the current money in the machine.
    :return: a tuple of the current water, current milk, current coffee beans, current disposable cups and current money
    """
    print()
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    coffee_type = input()
    match coffee_type :
        case "1":
            current_water, current_coffee_beans, current_disposable_cups, current_money = espresso(current_water, current_coffee_beans, current_disposable_cups, current_money)
        case "2":
            current_water, current_milk, current_coffee_beans, current_disposable_cups, current_money = latte(current_water, current_milk, current_coffee_beans, current_disposable_cups, current_money)
        case "3":
            current_water, current_milk, current_coffee_beans, current_disposable_cups, current_money = cappuccino(current_water, current_milk, current_coffee_beans, current_disposable_cups, current_money)
        case "back":
            pass
        case _:
            print("Invalid action")
    return current_water, current_milk, current_coffee_beans, current_disposable_cups, current_money


def espresso(current_water: int, current_coffee_beans: int, current_disposable_cups: int, current_money: int) -> tuple :
    """Handle the machine when the user chooses to buy an espresso.

    :param current_water: the current water in the machine.
    :param current_coffee_beans: the current coffee beans in the machine.
    :param current_disposable_cups: the current disposable cups in the machine.
    :param current_money: the current money in the machine.
    :return: a tuple of the current water, current coffee beans, current disposable cups and current money
    """
    if current_water < 250 or current_coffee_beans < 16 or current_disposable_cups < 1:
        deal_not_enough("espresso", current_water, current_coffee_beans, current_disposable_cups)
    else:
        print("I have enough resources, making you a coffee!")
        current_water -= 250
        current_coffee_beans -= 16
        current_disposable_cups -= 1
        current_money += 4
    return current_water, current_coffee_beans, current_disposable_cups, current_money


def latte(current_water: int, current_milk: int, current_coffee_beans: int, current_disposable_cups: int, current_money: int) -> tuple:
    """Handle the machine when the user chooses to buy a latte.

    :param current_water: the current water in the machine.
    :param current_milk: the current milk in the machine.
    :param current_coffee_beans: the current coffee beans in the machine.
    :param current_disposable_cups: the current disposable cups in the machine.
    :param current_money: the current money in the machine.
    :return: a tuple of the current water, current milk, current coffee beans, current disposable cups and current money
    """
    if current_water < 350 or current_milk < 75 or current_coffee_beans < 20 or current_disposable_cups < 1:
        deal_not_enough("latte", current_water, current_coffee_beans, current_disposable_cups, current_milk)
    else:
        print("I have enough resources, making you a coffee!")
        current_water -= 350
        current_milk -= 75
        current_coffee_beans -= 20
        current_disposable_cups -= 1
        current_money += 7
    return current_water, current_milk, current_coffee_beans, current_disposable_cups, current_money


def cappuccino(current_water: int, current_milk: int, current_coffee_beans: int, current_disposable_cups: int, current_money: int) -> tuple :
    """Handle the machine when the user chooses to buy a cappuccino.

    :param current_water: the current water in the machine.
    :param current_milk: the current milk in the machine.
    :param current_coffee_beans: the current coffee beans in the machine.
    :param current_disposable_cups: the current disposable cups in the machine.
    :param current_money: the current money in the machine.
    :return: a tuple of the current water, current milk, current coffee beans, current disposable cups and current money
    """
    if current_water < 200 or current_milk < 100 or current_coffee_beans < 12 or current_disposable_cups < 1:
        deal_not_enough("cappuccino", current_water, current_coffee_beans, current_disposable_cups, current_milk)
    else:
        print("I have enough resources, making you a coffee!")
        current_water -= 200
        current_milk -= 100
        current_coffee_beans -= 12
        current_disposable_cups -= 1
        current_money += 6
    return current_water, current_milk, current_coffee_beans, current_disposable_cups, current_money


def fill_action(current_water: int, current_milk: int, current_coffee_beans: int, current_disposable_cups: int, current_money: int) -> tuple :
    """Handle the machine when the user chooses to fill the machine.

    :param current_water: the current water in the machine.
    :param current_milk: the current milk in the machine.
    :param current_coffee_beans: the current coffee beans in the machine.
    :param current_disposable_cups: the current disposable cups in the machine.
    :param current_money: the current money in the machine.
    :return: a tuple of the current water, current milk, current coffee beans, current disposable cups and current money
    """
    print()
    print("Write how many ml of water you want to add:")
    current_water += int(input())
    print("Write how many ml of milk you want to add:")
    current_milk += int(input())
    print("Write how many grams of coffee beans you want to add:")
    current_coffee_beans += int(input())
    print("Write how many disposable cups you want to add:")
    current_disposable_cups += int(input())
    return current_water, current_milk, current_coffee_beans, current_disposable_cups, current_money


def take_action(current_money: int) -> int:
    """Handle the machine when the user chooses to take the money from the machine.

    :param current_money: the current money in the machine.
    :return: the current money in the machine.
    """
    print()
    print(f"I gave you ${current_money}")
    current_money = 0
    return current_money


def deal_not_enough(type_of_coffee: str, current_water: int, current_coffee_beans: int, current_disposable_cups: int, current_milk=0) -> None:
    """Handle the machine when there is less ingredient than needed.

    :param type_of_coffee: the type of the coffee the user wants to make
    :param current_water: the current water in the machine.
    :param current_coffee_beans: the current coffee beans in the machine.
    :param current_disposable_cups: the current disposable cups in the machine.
    :param current_milk: the current milk in the machine.
    """
    if (type_of_coffee == "espresso" and current_water < 250
        or type_of_coffee == "latte" and current_water < 350
        or type_of_coffee == "cappuccino" and current_water < 200):
        print("Sorry, not enough water!")
    elif (type_of_coffee == "latte" and current_milk < 75
        or type_of_coffee == "cappuccino" and current_milk < 100):
        print("Sorry, not enough milk!")
    elif (type_of_coffee == "espresso" and current_coffee_beans < 16
        or type_of_coffee == "latte" and current_coffee_beans < 20
        or type_of_coffee == "cappuccino" and current_coffee_beans < 12):
        print("Sorry, not enough coffee beans!")
    elif current_disposable_cups < 1:
        print("Sorry, not enough disposable cups!")


def main():
    """The main function of the coffee machine.
    """
    current_water = 400
    current_milk = 540
    current_coffee_beans = 120
    current_disposable_cups = 9
    current_money = 550

    while True:
        print("Write action (buy, fill, take, remaining, exit):")
        action = input()
        if action == "exit":
            break
        current_water, current_milk, current_coffee_beans, current_disposable_cups, current_money = get_action(action, current_water, current_milk, current_coffee_beans, current_disposable_cups, current_money)
        print()


if __name__ == "__main__":
    main()