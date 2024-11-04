#!/usr/bin/env python3
"""
project_02: 2nd project (Bulls & Cows) to ENGETO Online Python Academy   

author: Martin Alex Urbiš
email: urbis.martin@gmail.com
discord: segen0
"""

""" change log

* 03-11-2024 *
1) a different method was used to generate the random number
2) because of 1) the def 'secret_number_validation' was canceled
3) def 'check_guess_no_duplicity' - modified
4) def 'def bull_evaluation' - replaced  by def 'score_evaluation'
5) def 'def cow_evaluation' - replaced  by def 'score_evaluation'
6) the business logic of comparison SN and user's guess reworked

"""

import random

# variable declaration
secret_number: str  # secret 4-digit number
users_guess: str  # user's tip
secret_number_valid: bool = False  # SN is valid and game can begin
users_guess_valid: bool = False  # user's guess is valid for matching with SN
results_of_validation: list = list()  # individual results of validations
bull: int = 0  # number of bull's guesses
cow: int = 0  # number of cow's guesse


def secret_number_generation() -> str:
    """generation of secret number
    - 4 digits
    - no duplicity digits
    - without leading zero
    """
    sn_components = random.sample(range(0, 10), 5)
    conv_list = int("".join(map(str, sn_components)))
    conv_str = str(conv_list)

    return conv_str[:4]


# user guess validation functions
def check_length_user_guess(input: str) -> str:
    """check if the length of user's input is four chars"""
    if len(input) == 4:
        return "1"
    else:
        return "- incorrect input length (greater or less than 4 digits)."


def check_guess_is_number(input: str) -> str:
    """check if the user's input is number"""
    if input.isnumeric():
        return "1"
    else:
        return "- the input consists of alphabet characters - please enter only digits."


def check_guess_no_duplicity(input: str) -> str:
    """check individual component uniqueness"""
    if len(input) == 4:
        if len(set(input)) == 4:
            return "1"
        else:
            return "- there must be no duplicate digits in the number."
    else:
        # length does not meet with required value (4) but still evaluated like o.k.
        # because length is already evaluated in def 'check_length_user_guess'
        return "1"


def check_guess_has_leading_zero(input: str) -> str:
    """check if the user's input has a leading zero"""
    if input.startswith("0") is not True:
        return "1"
    else:
        return "- the number must not start with zero."


# evaluations and game over output functions
def score_evaluation(bull: int, cow: int) -> list:
    """cows / bulls evaluation"""
    bulls: str
    cows: str

    if bull == 1:
        bulls = str(bull) + " bull"
    else:
        bulls = str(bull) + " bulls"
    if cow == 1:
        cows = str(cow) + " cow"
    else:
        cows = str(cow) + " cows"

    return [bulls, cows]


def game_over_output(input: int) -> str:
    """game over result statement"""
    if number_of_guesses <= 2:
        return "That's amazing!"
    elif number_of_guesses >= 3 and number_of_guesses < 6:
        return "That's average!"
    elif number_of_guesses >= 6 and number_of_guesses < 11:
        return "Not so good ..."
    else:
        return "There's room for improvement, try again ..."


# initial part - welcome and SN generation
print("Hi there!")
print("-----------------------------------------------")
print(
    "I've generated a random 4 digit number for you. \nLet's play a bulls and cows game."
)
print("-----------------------------------------------")

# secret number generation
secret_number = secret_number_generation()

print("required SN: ", secret_number)  # TODO REMOVE ME in PROD release!

# main part - game
game_over: bool = False  # flag the SN and user's guess matach
number_of_guesses: int = 0  # number of attempts guess the secret number

while game_over is not True:

    # user's input and validation
    pass_input_validation: int = 0  # flag the user's input is o.k.
    users_guess = input("Enter a number (four digits): ")

    while pass_input_validation != 4:

        # check if the user's input is blank ("")
        while users_guess == "":
            print("There is no input on command line from you.\n")
            users_guess = input("Enter a number (four digits): ")

        # individual checks
        results_of_validation.append(check_length_user_guess(users_guess))
        results_of_validation.append(check_guess_is_number(users_guess))
        results_of_validation.append(check_guess_no_duplicity(users_guess))
        results_of_validation.append(check_guess_has_leading_zero(users_guess))

        # evaluation of user's input - all checks should finish with value "1"
        for item in results_of_validation:
            if item == "1":
                pass_input_validation = pass_input_validation + int(item)

        if pass_input_validation != 4:
            # user's input is not valid
            print("\nErrors found in user input:")
            for i in results_of_validation:
                if i != "1":
                    print(i)
            print()
            results_of_validation.clear()
            pass_input_validation = 0
            users_guess = input("Enter a number (four digits): ")
        else:
            # user's input is valid
            results_of_validation.clear()
            break

    # comparison SN and user's guess
    number_of_guesses = number_of_guesses + 1

    for i in range(0, 4):
        for letter in enumerate(users_guess):
            if (i == letter[0]) and (secret_number[i] == letter[1]):
                bull = bull + 1
            elif secret_number[i] == letter[1]:
                cow = cow + 1

    if users_guess != secret_number:
        result_evaluation: list = score_evaluation(bull, cow)
        print(result_evaluation[0], result_evaluation[1])
        bull = 0
        cow = 0
        print("\nYours guess does not match, next turn ...\n")

    else:
        # game over
        game_over = True

# game over and final result statement
print(
    f"Correct, you've guessed the right number in {number_of_guesses} guesses!"
)
print("---------------------------------------------")

print(game_over_output(number_of_guesses))
print()
