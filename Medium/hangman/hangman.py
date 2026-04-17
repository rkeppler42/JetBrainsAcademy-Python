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


def give_tip(word: str) -> str:
    """Prints the first three letters of the word.

    :param word: a given word
    :return: the three letters of the word followed by dashes
    """
    tip = word[:3] + (len(word) - 3) * "-"
    return tip

def guess_word(word: str, tip: str) -> None:
    """Asks the user to guess the word and checks if the guess is correct.

    :param word: the word to guess
    :param tip: the tip message
    """
    guess = input(f"Guess the word {tip}: > ")
    if guess == word:
        print("You survived!")
    else:
        print("You lost!")


def main() -> None:
    """The main function of the game."""
    show_title()
    list_of_words = ["python", "java", "swift", "javascript"]
    word = choose_word(list_of_words)
    tip = give_tip(word)
    guess_word(word, tip)


if __name__ == "__main__":
    main()
