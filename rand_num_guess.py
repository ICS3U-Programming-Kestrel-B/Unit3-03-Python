#!/usr/bin/env python3

# Created By: Kestrel Bryce
# Date: Oct. 6, 2022
# This program asks for a number
# between 1 and 9, and then tells
# you if your guess was correct
# based on a random correct answer

import math


def main():
    # input
    print("This program asks for a number")
    print("between 1 and 9, and then tells")
    print("you if your guess was correct")
    print("")
    user_guess = int(input("Enter a number between 1 and 9: "))

    # process/output
    # generating a random correct answer
    import random
    random_answer = random.randint(0, 9)

    if user_guess == random_answer:
        print("Your guess was correct!")
    else:
        print("Your guess was incorrect.")
        print("The correct answer was {}.".format(random_answer))


if __name__ == "__main__":
    main()
