import random

print("So in this game, you're to guess a number within a certain range correctly")

user_number = input("So type a number that would serve as the range.\n")
if user_number.isdigit():
    user_number = int(user_number)
    if user_number == 0:
        print("Please input a number greater than zero")
        quit()
else:
    print("TRY TYPING A NUMBER NEXT TIME!")
    quit()

random_number = random.randint(0, int(user_number))
guesses = 0

while True:
    guesses += 1
    print("Make a guess")
    guess = input()
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Type a number next time")
        continue

    if guess == random_number:
        print("You got it right!")
        break
    elif guess < random_number:
        print("You guessed below the number!")
        continue
    else:
        print("You guessed above the number!")
        continue