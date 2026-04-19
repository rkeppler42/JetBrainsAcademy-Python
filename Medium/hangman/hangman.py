import random
import string


def show_title() -> None:
    """Prints the title of the game."""
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


def process_user_guess(
    word: str, hidden_word: str, guess: str, attempts: int, letters_attempted: list
) -> tuple[str, int, list]:
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
    letters_attempted.append(guess)
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


def print_bye(word: str, hidden_word: str) -> None:
    """Prints the exit message.

    :param word: the random word the user has to guess
    :param hidden_word: the hidden word with the user attempts
    """
    if word == hidden_word:
        print(f"You guessed the word {word}!")
        print("You survived!")
    else:
        print("You lost!")


def main() -> None:
    """The main function of the game."""
    attempts = 8
    letters_attempted = []
    show_title()
    list_of_words = ["python", "java", "swift", "javascript"]
    word = choose_word(list_of_words)
    hidden_word = hide_word(word)
    while attempts > 0 and hidden_word != word:
        print_hidden_word(hidden_word)
        guess = input("Input a letter: > ")
        hidden_word, attempts, letters_attempted = process_user_guess(
            word, hidden_word, guess, attempts, letters_attempted
        )
    print_bye(word, hidden_word)


if __name__ == "__main__":
    main()
