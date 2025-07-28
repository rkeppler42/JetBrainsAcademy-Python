dictionary_of_friends = {}
counter = 0

print("Enter the number of friends joining (including you):")
number_of_friends = int(input())
print()

if number_of_friends > 0:
    print("Enter the name of every friend (including you), each on a new line:")
    while counter < number_of_friends:
        name_of_friend = input()
        dictionary_of_friends[name_of_friend] = 0
        counter += 1

    print(dictionary_of_friends)
else:
    print("No one is joining for the party")
