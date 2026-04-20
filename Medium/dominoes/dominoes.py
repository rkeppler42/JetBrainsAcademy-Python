import random


def print_header() -> None:
    """Prints the header of the game."""
    print("=" * 70)


def generate_dominoes() -> list:
    """Generates the dominoes that will take part in the game.

    :return: list of dominoes that will take part in the game
    """
    dominoes = [[i, j] for i in range(7) for j in range(i, 7)]
    return dominoes


def shuffle_dominoes(dominoes: list) -> None:
    """Shuffles the dominoes that will take part in the game.

    :param dominoes: list of dominoes that will take part in the game
    """
    random.shuffle(dominoes)


def find_starting_piece(dominoes: list) -> tuple[list, int] | None:
    """Finds the snake piece (the biggest double in the pile).

    :param dominoes: list of dominoes that will take part in the game
    :return: the snake piece if there is at least one piece with two equal values, None otherwise
    """
    greatest = [-1, -1]
    is_game_valid = False
    position = -1
    for i in range(14, len(dominoes)):
        if dominoes[i][0] == dominoes[i][1]:
            is_game_valid = True
            if dominoes[i][0] > greatest[0]:
                greatest = [dominoes[i][0], dominoes[i][1]]
                position = i
    if is_game_valid:
        return greatest, position
    return None


def distribute_dominoes(dominoes: list) -> tuple[list, list, list]:
    """Distributes the dominoes that will take part in the game to the player and to the computer.

    :param dominoes: list of dominoes that will take part in the game
    :return: tuple with the stock, computer and user pieces
    """
    stock_pieces = dominoes[:14]
    computer_pieces = dominoes[14:21]
    user_pieces = dominoes[21:]
    return stock_pieces, computer_pieces, user_pieces


def determine_who_starts(position: int) -> str:
    """Determines who starts the game.

    :param position: position of the domino snake piece
    :return: who starts the game
    """
    if position < 21:
        return "player"
    else:
        return "computer"


def remove_snake_piece(
    first_player: str, computer_pieces: list, user_pieces: list, domino_snake: list
) -> tuple[list, list]:
    """Removes snake piece from user or computer pieces.

    :param first_player: the player who starts the game
    :param computer_pieces: the computer pieces
    :param user_pieces: the user pieces
    :param domino_snake: the domino snake piece
    :return: a tuple with the computer pieces and the user pieces
    """
    if first_player == "player":
        computer_pieces.remove(domino_snake)
    else:
        user_pieces.remove(domino_snake)
    return computer_pieces, user_pieces


def print_status(
    stock_pieces: list,
    computer_pieces: list,
    user_pieces: list,
    domino_snake: list,
    first_player: str,
) -> None:
    """Prints the status of the game.

    :param stock_pieces: the stock pieces
    :param computer_pieces: the computer pieces
    :param user_pieces: the user pieces
    :param domino_snake: the domino snake piece
    :param first_player: the player who starts the game
    """
    print(f"Stock size: {len(stock_pieces)}")
    print(f"Computer pieces: {len(computer_pieces)}")
    print()
    print(domino_snake)
    print()
    print("Your pieces:")
    for i, piece in enumerate(user_pieces):
        print(f"{i + 1}:{piece}")
    print()
    if first_player == "player":
        print("Status: It's your turn to make a move. Enter your command.")
    else:
        print("Status: Computer is about to make a move. Press Enter to continue...")


def main() -> None:
    """Entry point of the game setup"""
    print_header()
    dominoes = generate_dominoes()
    snake = None
    while snake is None:
        shuffle_dominoes(dominoes)
        result = find_starting_piece(dominoes)
        if result is not None:
            snake, position = result
    stock_pieces, computer_pieces, user_pieces = distribute_dominoes(dominoes)
    first_player = determine_who_starts(position)
    computer_pieces, user_pieces = remove_snake_piece(
        first_player, computer_pieces, user_pieces, snake
    )
    print_status(stock_pieces, computer_pieces, user_pieces, snake, first_player)


if __name__ == "__main__":
    main()
