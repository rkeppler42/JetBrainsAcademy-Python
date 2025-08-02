import random


def ask_number_friends() -> int:
    print("Enter the number of friends joining (including you):")
    return int(input())


def populate_dictionary(count: int) -> dict:
    print("Enter the name of every friend (including you), each on a new line:")
    return {input(): 0 for _ in range(count)}


def get_total_bill() -> float:
    print("Enter the total bill value:")
    return float(input())


def split_bill(friends: dict, total: float) -> dict:
    price_per_person = round(total / len(friends), 2)
    return {friend: price_per_person for friend in friends}


def ask_use_lucky_feature() -> bool:
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    return input() == "Yes"


def pick_lucky_friend(dictionary_of_friends) -> str:
    return random.choice(list(dictionary_of_friends.keys()))


number_of_friends = ask_number_friends()
print()

if number_of_friends > 0:
    dict_of_friends = populate_dictionary(number_of_friends)
    print()
    total_bill = get_total_bill()
    value_per_friend = split_bill(dict_of_friends, total_bill)
    print()
    who_is_lucky = ask_use_lucky_feature()
    print()
    if who_is_lucky:
        lucky_one = pick_lucky_friend(value_per_friend)
        print(f"{lucky_one} is the lucky one!")
    else:
        print("No one is going to be lucky")
else:
    print("No one is joining for the party")