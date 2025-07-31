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
    print()
    print("Enter the total bill value:")
    total_bill_value = float(input())
    price_per_person = round(total_bill_value / number_of_friends, 2)
    for person in dictionary_of_friends:
        dictionary_of_friends[person] = price_per_person
    print(dictionary_of_friends)
else:
    print("No one is joining for the party")