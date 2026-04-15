import random


print("H A N G M A N")
list_of_words = ["python", "java", "swift", "javascript"]
word = random.choice(list_of_words)
guess = input("Guess the word: > ")
if guess == word:
    print("You survived!")
else:
    print("You lost!")