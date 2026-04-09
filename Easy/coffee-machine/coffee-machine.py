
def show_current_state(current_water: int, current_milk: int, current_coffee_beans: int, current_disposable_cups: int, current_money: int) -> None:
    """Print the current state of the coffee machine

    :param current_water: the current water in the machine.
    :param current_milk: the current milk in the machine.
    :param current_coffee_beans: the current coffee beans in the machine.
    :param current_disposable_cups: the current disposable cups in the machine.
    :param current_money: the current money in the machine.
    """
    print("The coffee machine has:")
    print(f"{current_water} ml of water")
    print(f"{current_milk} ml of milk")
    print(f"{current_coffee_beans} g of coffee beans")
    print(f"{current_disposable_cups} disposable cups")
    print(f"${current_money} of money")
    print()


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
    print("What do you want to buy?  1 - espresso, 2 - latte, 3 - cappuccino:")
    coffee_type = input()
    match coffee_type :
        case "1":
            current_water, current_coffee_beans, current_disposable_cups, current_money = espresso(current_water, current_coffee_beans, current_disposable_cups, current_money)
        case "2":
            current_water, current_milk, current_coffee_beans, current_disposable_cups, current_money = latte(current_water, current_milk, current_coffee_beans, current_disposable_cups, current_money)
        case "3":
            current_water, current_milk, current_coffee_beans, current_disposable_cups, current_money = cappuccino(current_water, current_milk, current_coffee_beans, current_disposable_cups, current_money)
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
    current_water -= 250
    current_coffee_beans -= 16
    current_disposable_cups -= 1
    current_money += 4
    return current_water, current_coffee_beans, current_disposable_cups, current_money


def latte(current_water: int, current_milk: int, current_coffee_beans: int, current_disposable_cups: int, current_money: int) -> tuple:
    """Handle the machine when the user chooses to buy a late.

    :param current_water: the current water in the machine.
    :param current_milk: the current milk in the machine.
    :param current_coffee_beans: the current coffee beans in the machine.
    :param current_disposable_cups: the current disposable cups in the machine.
    :param current_money: the current money in the machine.
    :return: a tuple of the current water, current milk, current coffee beans, current disposable cups and current money
    """
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
    :return: the current money in the machine."""
    print(f"I gave you ${current_money}")
    current_money = 0
    return current_money

def main():
    """The main function of the coffee machine.
    """
    current_water = 400
    current_milk = 540
    current_coffee_beans = 120
    current_disposable_cups = 9
    current_money = 550

    show_current_state(current_water, current_milk, current_coffee_beans, current_disposable_cups, current_money)
    print("Write action (buy, fill, take):")
    action = input()
    current_water, current_milk, current_coffee_beans, current_disposable_cups, current_money = get_action(action, current_water, current_milk, current_coffee_beans, current_disposable_cups, current_money)
    print()
    show_current_state(current_water, current_milk, current_coffee_beans, current_disposable_cups, current_money)


if __name__ == "__main__":
    main()