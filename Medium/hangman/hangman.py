import random
import string

WORDS = ["python", "java", "swift", "javascript"]


def show_title() -> None:
    """Show the title of the game."""
    print("H A N G M A N")


def show_menu() -> str:
    """Handle the menu of the game.

    :return: user input
    """
    user_input = input(
        'Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: > '
    )
    return user_input


def choose_word(list_of_words: list[str]) -> str:
    """Choose a random word from a list of words.

    :param list_of_words: list of words
    :return: random word
    """
    word = random.choice(list_of_words)
    return word


def hide_word(word: str) -> str:
    """Hide a given word from the user.

    :param word: word
    :return: hidden word
    """
    return "-" * len(word)


def print_hidden_word(hidden_word: str) -> None:
    """Print the hidden word from the user.

    :param hidden_word: hidden word
    """
    print()
    print(hidden_word)


def process_user_guess(
    word: str, hidden_word: str, guess: str, attempts: int, letters_attempted: set[str]
) -> tuple[str, int, set]:
    """Process the user guess.

    :param word: the random word the user has to guess
    :param hidden_word: the hidden word the user has to guess
    :param guess: the guessed letter
    :param attempts: the number of times that the user can guess wrongly
    :param letters_attempted: the letters already guessed
    :return: hidden word and number of attempts still has
    """
    if (
        len(guess) != 1
        or guess not in string.ascii_lowercase
        or guess in letters_attempted
    ):
        if len(guess) != 1:
            print("Please, input a single letter.")
            return hidden_word, attempts, letters_attempted
        elif guess in letters_attempted:
            print("You've already guessed this letter.")
            return hidden_word, attempts, letters_attempted
        else:
            print("Please, enter a lowercase letter from the English alphabet.")
            return hidden_word, attempts, letters_attempted
    letters_attempted.add(guess)
    if guess in word and guess not in hidden_word:
        for i in range(len(word)):
            if word[i] == guess:
                hidden_word = hidden_word[:i] + guess + hidden_word[i + 1 :]
    else:
        if guess in hidden_word:
            print("No improvements.")
        else:
            print("That letter doesn't appear in the word.")
        attempts -= 1
    return hidden_word, attempts, letters_attempted


def handle_game_result(
    word: str, hidden_word: str, games_won: int, games_lost: int
) -> tuple[int, int]:
    """Handle the game result and updates the scoreboard.

    :param word: the random word the user has to guess
    :param hidden_word: the hidden word with the user attempts
    :param games_won: the number of games won
    :param games_lost: the number of games lost
    :return: the number of games won and the number of games lost
    """
    if word == hidden_word:
        print(f"You guessed the word {word}!")
        print("You survived!")
        games_won += 1
        return games_won, games_lost
    else:
        print("You lost!")
        games_lost += 1
        return games_won, games_lost


def show_results(games_won: int, games_lost: int) -> None:
    """Show the results of the game.

    :param games_won: the number of games won
    :param games_lost: the number of games lost
    """
    print(f"You won: {games_won} times.")
    print(f"You lost: {games_lost} times.")


def main() -> None:
    """The main function of the game."""
    games_won = 0
    games_lost = 0
    show_title()
    user_input = show_menu()
    while user_input != "exit":
        if user_input == "play":
            attempts = 8
            letters_attempted = set()

            word = choose_word(WORDS)
            hidden_word = hide_word(word)
            while attempts > 0 and hidden_word != word:
                print_hidden_word(hidden_word)
                guess = input("Input a letter: > ")
                hidden_word, attempts, letters_attempted = process_user_guess(
                    word, hidden_word, guess, attempts, letters_attempted
                )
            games_won, games_lost = handle_game_result(
                word, hidden_word, games_won, games_lost
            )
        if user_input == "results":
            show_results(games_won, games_lost)
        user_input = show_menu()


if __name__ == "__main__":
    main()
