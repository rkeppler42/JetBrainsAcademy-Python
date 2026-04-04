def number_of_pencils() -> int:
    """Asks the user to enter how many pencils will be used in the game.

    :return: the number of pencils that will be used in the game.
    """
    print("How many pencils would you like to use:")
    num_of_pencils = int(input())
    return num_of_pencils


def define_first_player() -> list:
    """Defines the first player who will play the game.

    :return: a list of players where list[0] is the first player and the list[1] is the second player.
    """
    print("Who will be the first (John, Jack):")
    first_player = input()
    if first_player == "John":
        return ["John", "Jack"]
    return ["Jack", "John"]


def print_pencils(num_pencils: int) -> None:
    """Prints the number of pencils that are in use in the game.

    :param num_pencils: the number of pencils remaining in the game.
    """
    print("|" * num_pencils)


def print_player_turn(player_order: list, player_count: int) -> None:
    """Prints the player who will play the game in this turn.

    :param player_order: the players in order of play.
    :param player_count: the player who will play the game in this turn.
    """
    if player_count % 2 == 0:
        print(f"{player_order[0]}'s turn:")
    else:
        print(f"{player_order[1]}'s turn:")



def main_game_loop(num_pencils: int, player_order: list) -> None:
    """The main game loop.

    :param num_pencils: the number of pencils remaining in the game.
    :param player_order: the list of players who will play the game.
    """
    player_count = 0
    while num_pencils > 0:
        print_pencils(num_pencils)
        print_player_turn(player_order, player_count)
        player_move = int(input())
        num_pencils -= player_move
        player_count += 1


def main():
    n_of_pencils = number_of_pencils()
    player_order = define_first_player()
    main_game_loop(n_of_pencils, player_order)


if __name__ == "__main__":
    main()