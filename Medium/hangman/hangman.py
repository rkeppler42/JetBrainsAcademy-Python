import random


def show_title() -> None:
    """Prints the title of the game.
    """
    print("H A N G M A N")


def choose_word(list_of_words: list) -> str:
    """Chooses a random word from a list of words.

    :param list_of_words: list of words
    :return: random word
    """
    word = random.choice(list_of_words)
    return word


def hide_word(word: str) -> str:
    """Hides a given word from the user.

    :param word: word
    :return: hidden word
    """
    return "-" * len(word)


def print_hidden_word(hidden_word: str) -> None:
    """Prints the hidden word from the user.

    :param hidden_word: hidden word
    """
    print()
    print(hidden_word)


def process_user_guess(word: str, hidden_word: str, guess: str) -> str:
    """Process the user guess.

    :param word: the random word the user has to guess
    :param hidden_word: the hidden word the user has to guess
    :param guess: the guessed letter
    :return: the hidden word with the right user guess
    """
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                hidden_word = hidden_word[:i] + guess + hidden_word[i+1:]
    else:
        print("That letter doesn't appear in the word.")
    return hidden_word


def print_bye() -> None:
    """Prints the exit message."""
    print()
    print("Thanks for playing!")


def main() -> None:
    """The main function of the game."""
    attempts = 8
    show_title()
    list_of_words = ["python", "java", "swift", "javascript"]
    word = choose_word(list_of_words)
    hidden_word = hide_word(word)
    while attempts > 0:
        print_hidden_word(hidden_word)
        guess = input("Input a letter: > ")
        hidden_word = process_user_guess(word, hidden_word, guess)
        attempts -= 1
    print_bye()


if __name__ == "__main__":
    main()
