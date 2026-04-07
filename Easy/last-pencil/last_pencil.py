import random
from typing import Literal


class InvalidNumberOfPencils(Exception):
    pass

def number_of_pencils() -> int:
    """Asks the user to enter how many pencils will be used in the game.

    :return: the number of pencils that will be used in the game.
    """
    print("How many pencils would you like to use:")
    while True:
        try:
            num_pencils = int(input())
            if num_pencils < 0:
                raise ValueError
            if num_pencils == 0:
                raise InvalidNumberOfPencils
            break
        except ValueError:
            print("The number of pencils should be numeric")
        except InvalidNumberOfPencils:
            print("The number of pencils should be positive")
    return num_pencils



def define_first_player() -> Literal["John", "Jack"]:
    """Defines the first player who will play the game.

    :return: returns the first player who will play the game.
    """
    print("Who will be the first (John, Jack):")
    first_player = input()
    while first_player not in ["John", "Jack"]:
        first_player = input("Choose between John and Jack:\n")
    return first_player


def print_pencils(num_pencils: int) -> None:
    """Prints the number of pencils that are in use in the game.

    :param num_pencils: the number of pencils remaining in the game.
    """
    if num_pencils > 0:
        print("|" * num_pencils)


def winner(who_wins: str) -> None:
    """Prints the winner of the game.

    :param who_wins: the player who wins.
    """
    print(f"{who_wins} won!")


def player_turn(num_of_pencils: int) -> tuple[int, int]:
    """Validates the player's move and if valid makes the move.

    :param num_of_pencils: the number of pencils remaining in the game.
    :return: the number of pencils remaining in the game after the player's turn and how many pencils were taken.
    """

    while True:
        player_move = input()
        if player_move not in ['1', '2', '3']:
            print("Possible values: '1', '2' or '3'")
        elif int(player_move) > num_of_pencils:
            print("Too many pencils were taken")
        else:
            return num_of_pencils - int(player_move), int(player_move)



def bot_turn(num_of_pencils: int) -> tuple[int, int]:
    """Emulates the bot's turn.

    :param num_of_pencils: the number of pencils remaining in the game.
    :return: the number of pencils remaining in the game after the bot's turn and how many pencils the bot took.
    """
    if num_of_pencils % 4 == 0:
        bot_move = 3
        return num_of_pencils - bot_move, bot_move
    if num_of_pencils % 4 == 3:
        bot_move = 2
        return num_of_pencils - bot_move, bot_move
    if num_of_pencils % 4 == 2:
        bot_move = 1
        return num_of_pencils - bot_move, bot_move
    if num_of_pencils == 1:
        bot_move = 1
        return num_of_pencils - bot_move, bot_move
    bot_move = random.randint(1, 3)
    return num_of_pencils - bot_move, bot_move


def main_game_loop(num_pencils: int, first_player: str) -> None:
    """The main game loop.

    :param num_pencils: the number of pencils remaining in the game.
    :param first_player: the player who will play the game first.
    """

    print_pencils(num_pencils)
    who_plays = first_player
    while num_pencils > 0:
        print(f"{who_plays}'s turn!")
        if who_plays == "John":
            num_pencils, player_move = player_turn(num_pencils)
            who_plays = "Jack"
        elif who_plays == "Jack":
            num_pencils, bot_move = bot_turn(num_pencils)
            print(bot_move)
            who_plays = "John"
        print_pencils(num_pencils)
    winner(who_plays)


def main():
    n_of_pencils = number_of_pencils()
    first_player = define_first_player()
    main_game_loop(n_of_pencils, first_player)


if __name__ == "__main__":
    main()