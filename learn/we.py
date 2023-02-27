import random

def play_game():
    name = input("Hello! What is your name?\n")
    print("Well, " + name + ", I am thinking of a number between 1 and 20.")

    # Generate a random number between 1 and 20
    number = random.randint(1, 20)
    guesses = 0

    while True:
        guess = int(input("Take a guess.\n"))
        guesses += 1

        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            break

    print("Good job, " + name + "! You guessed my number in " + str(guesses) + " guesses!")

play_game()
