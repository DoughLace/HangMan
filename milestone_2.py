import random
word_list = ["Animals", "Building", "Cuisine", "Defense", "Echo"]
print(word_list)

word = random.choice(word_list)
print(word)

guess = input("Enter a single letter ")
if len(guess) == 1:
    print("Good Guess!")
else:
    print("Oops! That is not a valid input.")
#print("your chosen letter is:", guess, "?")