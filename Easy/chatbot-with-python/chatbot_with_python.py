def greet(bot_name, birth_year):
    print(f"Hello! My name is {bot_name}.")
    print(f"I was created in {birth_year}.")


def remind_name():
    print("Please, remind me your name.")
    your_name = input()
    print(f"What a great name you have, {your_name}!")

def guess_age():
    print('Let me guess your age.')
    print("Enter remainders of dividing your age by 3, 5 and 7.")
    remainder_of_3 = int(input())
    remainder_of_5 = int(input())
    remainder_of_7 = int(input())
    your_age = (remainder_of_3 * 70 + remainder_of_5 * 21 + remainder_of_7 * 15) % 105
    print(f"Your age is {your_age}; that's a good time to start programming!")

def count():
    print("Now I will prove to you that I can count to any number you want.")
    number = int(input())
    counter = 0
    while counter <= number:
        print(counter, "!")
        counter += 1
    print("Completed, have a nice day!")


def test():
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")
    answer = int(input())
    while answer != 2:
        print("Please, try again.")
        answer = int(input())


def end():
    print('Congratulations, have a nice day!')


greet('Aid', '2025')  # change it as you need
remind_name()
guess_age()
count()
test()
end()
