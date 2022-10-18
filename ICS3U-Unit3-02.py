#!/usr/bin/env python3

# Created by: Emmanuel
# Created on: Oct 2022
# This program is a number guessing game


import constants


def main():

    # input
    guess_number = int(input("Guess a number from 0 - 9:"))

    # process and output
    if guess_number == constants.CONSTANT_NUMBER:
        print("\nYou guessed right.")
    if guess_number != constants.CONSTANT_NUMBER:
        print("\nYou guessed wrong, try again.")

    print("\n\nDone.")


if __name__ == "__main__":
    main()
