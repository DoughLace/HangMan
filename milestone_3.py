import random

### random word selecter -DONE-
def random_word():
    word_list = ["apple", "banana", "coconut", "mango", "kiwi"]
    word = random.choice(word_list)
    return word

selected_word = random_word()



### check if user input is in word -DONE-
def check_guess(guess, selected_word):
    guessed_letters = []
    for letter in guess:
        if letter in selected_word:
            guessed_letters.append(letter)
        else:
            guessed_letters.append("-")
    print("Current Word:", ''.join(guessed_letters))
    
    
### user input
def ask_for_input():
    while True:
        guess = input("Enter a letter: ")
        if guess.isalpha() and len(guess) == 1:
            guess = guess.lower()
            check_guess(guess, selected_word)
            return guess
        else:
            print("Invalid letter. Please, enter a single alphabetical letter.")
    


 
ask_for_input()