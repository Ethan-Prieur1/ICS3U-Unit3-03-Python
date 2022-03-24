#!/usr/bin/env python3

# Created by Ethan Prieur
# Created on March 2022
# This is a program that makes the user guess a number

import random


def main():
    # This Function Runs the Program

    # Input
    Number = int(input("Enter The Number You're Guessing (0-9):"))

    # Process & Output
    Hidden_Number = random.randint(0, 9)
    if Number == Hidden_Number:
        print("You Were Correct! Hooray! You're Lucky!")
    else:
        print("You Were Incorrect! You Fool! You Blundered!")


if __name__ == "__main__":
    main()
