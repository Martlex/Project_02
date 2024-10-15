#!/usr/bin/env python3
"""
project_02: 2nd project (Bulls & Cows) to ENGETO Online Python Academy   

author: Martin Alex Urbiš
email: urbis.martin@gmail.com
discord: segen0
"""
from random import randrange
from collections import Counter

# variable declaration
secret_number: str  # secret 4-digit number
users_guess: str  # user's tip
secret_number_valid: bool = False  # SN is valid and game can begin
users_guess_valid: bool = False  # user's guess is valid for matching with SN
results_of_validation: list = list()  # individual results of validations


def secret_number_generation() -> str:
    """generation of secret number
    - 4 digits
    - no duplicity digits
    - without leading zero
    """
    random_component: int = 0  # random component for secret number
    sn_output: str = ""  # secret number components / output

    for num in range(1, 5):
        random_component = randrange(10)
        while num == 1 and random_component == 0:
            random_component = randrange(10)
        else:
            sn_output = sn_output + str(random_component)

    return sn_output


# secret number validation functions
def secret_number_validation(sec_num: str) -> bool:
    """check secret number individual component uniqueness"""
    freq = Counter(sec_num)

    if len(freq) == len(sec_num):
        return True
    else:
        return False


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
    freq = Counter(input)

    if len(freq) == len(input):
        return "1"
    else:
        return "- there must be no duplicate digits in the number."


def check_guess_has_leading_zero(input: str) -> str:
    """check if the user's input has a leading zero"""
    if input.startswith("0") is not True:
        return "1"
    else:
        return "- the number must not start with zero."


# evaluations and game over output functions
def bull_evaluation(input: int) -> str:
    """evaluation for bull result"""
    if input == 1:
        return str(bull_score) + " bull"
    else:
        return str(bull_score) + " bulls"


def cow_evaluation(input: int):
    """evaluation for cow result"""
    if cow_score == 1:
        return str(cow_score) + " cow"
    else:
        return str(cow_score) + " cows"


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
while secret_number_valid is not True:
    secret_number = secret_number_generation()
    secret_number_valid = secret_number_validation(secret_number)

# print("required SN: ", secret_number)  # TODO REMOVE ME in PROD release!

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
            pass_input_validation = 0
            break

    # comparison SN and user's guess
    char_position: int = 0  # positon of element in the list (SN)
    bull_score: int = 0  # number of bull's guesses
    cow_score: int = 0  # number of cow's guesse
    cow_values: str = ""  # values for cow evaluation
    bulls_result: str = ""
    cows_result: str = ""

    # bulls evaluation
    number_of_guesses = number_of_guesses + 1
    for char in secret_number:
        if char == users_guess[char_position]:
            # the bright bulls
            bull_score = bull_score + 1
            char_position = char_position + 1
        else:
            # cow candidates
            cow_values = cow_values + users_guess[char_position]
            char_position = char_position + 1

    # cows evaluation (based on cow candidates)
    for char in cow_values:
        if secret_number.count(char) > 0:
            cow_score = cow_score + 1

    if bull_score == 4:
        game_over = True
    else:
        bulls_result = bull_evaluation(bull_score)
        cows_result = cow_evaluation(cow_score)

        print(f"{bulls_result}, {cows_result}")
        bull_score = 0
        cow_score = 0

    if users_guess != secret_number:
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
