""" Guess the number game. Has 2 modes:
1) Based on decimal number, guess its Roman equivalent.
2) Based on Roman numeral, guess its decimal equivalent.
The game give points for the right answer and substract points for the
wrong one. At the end of the game, total points are printed out to the screen.

The points are added and substracted based on following rules. Let's call
addition or substraction the "diff".
1) If number is in range [1, 99], then diff = 1.
2) If number is in range [100, 999], then diff = 2.
3) If number is greater than 999, then diff = 3.

All decimal and Roman numbers are in the range [1, 3999].

For more information on Roman numerals, please, see following articles:
https://en.wikipedia.org/wiki/Roman_numerals
https://projecteuler.net/about=roman_numerals
"""
import random
from time import time
from integer_to_roman import Solution as SolIntRom
from roman_to_integer import Solution as SolRomInt


sol_int_rom = SolIntRom()
sol_rom_int = SolRomInt()
integer_to_roman = sol_int_rom.int_to_roman
roman_to_integer = sol_rom_int.roman_to_int


def calculate_diff(number):
    """ Returns diff value for the number.
    """
    if number < 100:
        diff = 1
    elif 100 <= number <= 999:
        diff = 2
    else:
        diff = 3
    return diff


def guess_integer():
    """ Guess the integer based on Roman numeral game.
    """
    # introduction
    print("Welcome to the 'Guess the integer' game!")

    points = 0  # number of points
    while True:
        # generate random number, convert it to Roman numeral
        original_number = random.randrange(1, 4000)
        roman_number = integer_to_roman(original_number)
        diff = calculate_diff(original_number)

        print()
        print(f"What's the integer number for {roman_number}?")
        answer = input().strip()
        if answer == str(original_number):
            points += diff
            print("Well done!")
            print(f"Integer equivalent of {roman_number} is {answer}.")
        else:
            points -= diff
            print("Sorry. Wrong answer.")
            print(f"Integer equivalent of {roman_number} is {original_number}.")

        while True:
            choice = input("Enter c to continue the game or q to quit the game: ").strip().lower()
            if choice == "c":
                break
            elif choice == "q":
                print("Thank you for playing the game.")
                break
            else:
                print("I didn't understand your choice. Please, try again.")
        if choice == "c":
            continue
        else:
            break

    if points > 0:
        print(f"Well done! You got {points} points!")
    else:
        print(f"You got {points} points. Better luck next time.")


def guess_roman():
    """ Guess the Roman numeral based on integer game.
    """
    # introduction
    print("Welcome to the 'Guess the Roman' game!")

    points = 0  # number of points
    while True:
        # generate random integer number and convert it to Roman numeral
        integer_number = random.randrange(1, 4000)
        correct_roman = integer_to_roman(integer_number)
        diff = calculate_diff(integer_number)

        print()
        print(f"What's the Roman number for {integer_number}?")
        answer = input().strip().upper()
        if answer == correct_roman:
            points += diff
            print("Well done!")
            print(f"Roman equivalent of {integer_number} is {answer}.")
        else:
            points -= diff
            print("Sorry. Wrong answer.")
            print(f"Roman equivalent of {integer_number} is {correct_roman}.")

        while True:
            choice = input("Enter c to continue the game or q to quit the game: ").strip().lower()
            if choice == "c":
                break
            elif choice == "q":
                print("Thank you for playing the game.")
                break
            else:
                print("I didn't understand your choice. Please, try again.")
        if choice == "c":
            continue
        else:
            break

    if points > 0:
        print(f"Well done! You got {points} points!")
    else:
        print(f"You got {points} points. Better luck next time.")


def main():
    while True:
        print("Choose the game, please.\n")
        print("Enter 1 to play the game 'Guess the Roman numeral from integer',\
              \nor enter 2 to play the game 'Guess the integer from Roman numeral.'\n")
        print("Enter q or quit to quit the game.")
        print()
        choice = input("What do you choose? ").strip().lower()
        print()
        if choice == "1":
            guess_roman()
            break
        elif choice == "2":
            guess_integer()
            break
        elif choice.startswith("q"):
            print("Thank you for playing the game.")
            break
        else:
            print("Unknown choice. Try again, please.\n")


if __name__ == "__main__":
    main()
