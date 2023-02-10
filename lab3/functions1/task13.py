import random

def guess_number():
    print("Hello! What is your name?")
    name = input()
    print("Well, " + name + ", I am thinking of a number between 1 and 20.")
    secret_number = random.randint(1, 20)
    guess = 0
    tries = 0

    while guess != secret_number:
        print("Take a guess.")
        guess = int(input())
        tries += 1
        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")

    print("Good job, " + name + "! You guessed my number in " + str(tries) + " guesses!")

guess_number()
