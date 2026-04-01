"""Functions for splitting a bill among a group of friends.
"""
import random


def get_number_of_friends() -> int:
    """Get the number of friends joining.

    :return: number of friends.
    """
    print("Enter the number of friends joining (including you):")
    n_of_friends = int(input())
    print()
    return n_of_friends


def initialize_friends_dictionary(n_of_friends: int) -> dict:
    """Initialize a dictionary with friend names as keys and 0 as values.

    :param n_of_friends: number of friends.
    :return: dictionary with friend names as keys, each initialized to 0.
    """
    print("Enter the name of every friend (including you), each on a new line:")
    friends_dictionary = {}
    for _ in range(n_of_friends):
        friends_dictionary[input()] = 0
    print()
    return friends_dictionary


def bill_splitter(friends_dictionary: dict, total_bill: float, number_of_friends: int) -> dict:
    """Split bills among friends.

    :param friends_dictionary: dictionary with friend names as keys, each initialized to 0.
    :param total_bill: total bill.
    :param number_of_friends: number of friends.
    :return: dictionary with friend names as keys, with the value of the bill split among friends.
    """
    split_value = round(total_bill / number_of_friends, 2)
    for key in friends_dictionary:
        friends_dictionary[key] = split_value
    return friends_dictionary


def choice_friend(friends_dictionary: dict) -> str:
    """Choose a random friend from the dictionary.

    :param friends_dictionary: dictionary with friend names as keys, each initialized to 0.
    :return:  randomly selected friend's name.
    """
    return random.choice(list(friends_dictionary.keys()))


def bill_splitter_with_lucky(friends_dictionary: dict, total_bill: float, number_of_friends: int, lucky_one: str) -> dict:
    """Split bills among friends but lucky one pays 0.

    :param friends_dictionary: dictionary with friend names as keys, each initialized to 0.
    :param total_bill: total bill.
    :param number_of_friends: number of friends.
    :param lucky_one: lucky one.
    :return: dictionary with friend names as keys, with the value of the bill split among friends.
    """
    split_value = round(total_bill / (number_of_friends - 1), 2)
    for key in friends_dictionary:
        if key == lucky_one:
            friends_dictionary[key] = 0
        else:
            friends_dictionary[key] = split_value
    return friends_dictionary

def main():
    number_of_friends = get_number_of_friends()
    if number_of_friends <= 0:
        print()
        print("No one is joining for the party")
    else:
        f_dictionary = initialize_friends_dictionary(number_of_friends)
        total_bill = float(input("Enter the total bill value:\n"))
        user_choice = input('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:\n')
        print()
        if user_choice == 'Yes':
            lucky_one = choice_friend(f_dictionary)
            print(f"{lucky_one} is the lucky one!")
            print(bill_splitter_with_lucky(f_dictionary, total_bill, number_of_friends, lucky_one))
        else:
            print("No one is going to be lucky")
            print(bill_splitter(f_dictionary, total_bill, number_of_friends))

if __name__ == "__main__":
    main()