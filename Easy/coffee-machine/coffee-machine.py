from enum import Enum


class CoffeeMachine:
    """Represent a coffee machine with a state machine to handle user input.

    :ivar water: the current water in the machine in ml.
    :ivar milk: the current milk in the machine in ml.
    :ivar coffee_beans: the current coffee beans in the machine in g.
    :ivar disposable_cups: the current disposable cups in the machine.
    :ivar money: the current money in the machine in $.
    :ivar state: the current state of the machine.
    """

    class State(Enum):
        """Represent the possible states of the coffee machine."""
        MAIN = "MAIN"
        BUY = "BUY"
        FILL_WATER = "FILL_WATER"
        FILL_MILK = "FILL_MILK"
        FILL_BEANS = "FILL_BEANS"
        FILL_CUPS = "FILL_CUPS"
        EXIT = "EXIT"


    def __init__(self):
        """Initialize the coffee machine."""
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.disposable_cups = 9
        self.money = 550
        self.state = CoffeeMachine.State.MAIN


    def process_input(self, input_str: str) -> str | None:
        """Process the user input.

        :param input_str: the input to the machine.
        :return: the output of the machine.
        """
        match self.state:
            case CoffeeMachine.State.MAIN:
                output = self._handle_main(input_str)
                return output
            case CoffeeMachine.State.BUY:
                output = self._handle_buy(input_str)
                return output
            case CoffeeMachine.State.FILL_WATER:
                output = self._handle_fill_water(input_str)
                return output
            case CoffeeMachine.State.FILL_MILK:
                output = self._handle_fill_milk(input_str)
                return output
            case CoffeeMachine.State.FILL_BEANS:
                output = self._handle_fill_beans(input_str)
                return output
            case CoffeeMachine.State.FILL_CUPS:
                self._handle_fill_cups(input_str)
            case CoffeeMachine.State.EXIT:
                pass


    def _handle_main(self, cmd: str) -> str | None:
        """Handle the main menu.

        :param cmd: the input to the machine.
        :return: the output of the machine.
        """
        match cmd:
            case "remaining":
                output = self._status()
                return output
            case "buy":
                self.state = CoffeeMachine.State.BUY
                return "\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:"
            case "fill":
                self.state = CoffeeMachine.State.FILL_WATER
                return "\nWrite how many ml of water you want to add:"
            case "take":
                output = self._handle_take()
                return "\n" + output
            case "exit":
                self.state = CoffeeMachine.State.EXIT
        return None


    def _handle_buy(self, choice: str) -> str | None:
        """Handle the buy menu.

        :param choice: the input to the machine.
        :return: the output of the machine.
        """
        match choice:
            case "1":
                output = self._check_resources(250, 0, 16, 1, 4)
                return output
            case "2":
                output = self._check_resources(350, 75, 20, 1, 7)
                return output
            case "3":
                output = self._check_resources(200, 100, 12, 1, 6)
                return output
            case "back":
                self.state = CoffeeMachine.State.MAIN
                return None
            case _:
                return "Invalid choice"


    def _handle_fill_water(self, val: str) -> str:
        """Handle the fill water action.

        :param val: the ml of water you want to add to the machine.
        :return: the output of the machine.
        """
        val = int(val)
        self.water += val
        self.state = CoffeeMachine.State.FILL_MILK
        return "Write how many ml of milk you want to add:"


    def _handle_fill_milk(self, val: str) -> str:
        """Handle the fill milk action.

        :param val: the ml of milk you want to add to the machine.
        :return: the output of the machine.
        """
        val = int(val)
        self.milk += val
        self.state = CoffeeMachine.State.FILL_BEANS
        return "Write how many grams of coffee beans you want to add:"


    def _handle_fill_beans(self, val: str) -> str:
        """Handle the fill beans action.

        :param val: the g of coffee beans you want to add to the machine.
        :return: the output of the machine.
        """
        val = int(val)
        self.coffee_beans += val
        self.state = CoffeeMachine.State.FILL_CUPS
        return "Write how many disposable cups you want to add:"


    def _handle_fill_cups(self, val: str) -> None:
        """Handle the fill cups action.

        :param val: the quantity of disposable cups you want to add to the machine.
        """
        val = int(val)
        self.disposable_cups += val
        self.state = CoffeeMachine.State.MAIN


    def _check_resources(self, w: int, m: int, b: int, cups: int, price: int) -> str | None:
        """Check if the machine has enough resources to prepare the coffee.

        :param w: the water you need to do the type of coffee selected;
        :param m: the milk you need to do the type of coffee selected;
        :param b: the beans you need to do the type of coffee selected;
        :param cups: the cups you need to do the type of coffee selected;
        :param price: the price of the coffee you want to buy;
        :return: the output of the machine.
        """
        self.state = CoffeeMachine.State.MAIN
        if self.water >= w and self.milk >= m and self.coffee_beans >= b and self.disposable_cups >= cups:
            self.water -= w
            self.milk -= m
            self.coffee_beans -= b
            self.disposable_cups -= cups
            self.money += price
            return "\nI have enough resources, making you a coffee!"

        elif self.water < w:
            return "\nSorry, not enough water!"
        elif self.milk < m:
            return "\nSorry, not enough milk!"
        elif self.coffee_beans < b:
            return "\nSorry, not enough coffee beans!"
        elif self.disposable_cups < cups:
            return "\nSorry, not enough disposable cups!"
        return None


    def _handle_take(self) -> str:
        """Handle the take action.

        :return: the output of the machine.
        """
        current_money = self.money
        self.money = 0
        self.state = CoffeeMachine.State.MAIN
        return f"I gave you ${current_money}"


    def _status(self) -> str:
        """Handle the remaining action.

        :return: the output of the machine.
        """
        return (f"\nThe coffee machine has:\n"
                f"{self.water} ml of water\n"
                f"{self.milk} ml of milk\n"
                f"{self.coffee_beans} g of coffee beans\n"
                f"{self.disposable_cups} disposable cups\n"
                f"${self.money} of money\n")


def main():
    """The main function of the coffee machine.
    """
    coffee_machine = CoffeeMachine()

    while coffee_machine.state != CoffeeMachine.State.EXIT:
        if coffee_machine.state == CoffeeMachine.State.MAIN:
            print("Write action (buy, fill, take, remaining, exit):")
        user_input = input()
        output = coffee_machine.process_input(user_input)

        if output:
            print(output)



if __name__ == "__main__":
    main()