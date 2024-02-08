from random import *


# Function to check user's consent to play the game
def consent_check():
    while True:
        consent = input()
        if consent.lower() == 'yes':  # If the user consents to play
            print('Then let\'s begin!')  # Inform user the game is starting
            return True
        elif consent.lower() == 'no':  # If the user declines to play
            print('Too bad, perhaps another time...')  # Inform user they declined
            return False
        else:
            print('I couldn\'t understand. Do you want to play or not?')  # Prompt for clarification
            continue


# Function to determine the range of numbers for the game
def number_range():
    print(
        'Would you like to set a numerical range for the game? \nOr shall we play with standard rules from 0 to 100? \nEnter "YES" if you want to set a range or "NO" if we play by default.')
    while True:
        range_answer = input()
        if range_answer.lower() == 'yes':  # If user wants to set custom range
            print('Enter the left boundary: ')
            x = int(input())  # Input left boundary
            print('Enter the right boundary: ')
            y = int(input())  # Input right boundary
            print('Then let\'s begin!')  # Inform user the game is starting
            return randint(int(x), int(y))  # Return random number within custom range
        elif range_answer.lower() == 'no':  # If user chooses default range
            print(
                'Alright, let\'s play in the range from 1 to 100! Please enter a number:')  # Inform user about default range
            return randint(1, 100)  # Return random number within default range
        else:
            print('I couldn\'t understand. Will you choose the limits? Please try again!')  # Prompt for clarification
            continue


# Function to check if the user's input is a valid number
def is_valid(string):
    return string.isdigit() and 1 <= int(string) <= 100  # Check if the input is a digit between 1 and 100


# Welcome message
print('Welcome to the Number Guessing Game!')
print('Would you like to play? Enter "YES" if you do, or "NO" if you changed your mind!')

# Check user's consent to play
if consent_check() == True:
    number = number_range()  # Determine the number range for the game
    while True:
        user_number = input()  # Input user's guess
        if is_valid(user_number) == False:  # If the input is not valid
            print('Maybe let\'s input an integer from 1 to 100?')  # Prompt for a valid input
            continue
        if is_valid(user_number) == True:  # If the input is valid
            user_number = int(user_number)  # Convert user's input to integer
            if user_number < number:
                print('Your number is less than the hidden number, try again')  # Inform user their guess is too low
                continue
            elif user_number > number:
                print('Your number is greater than the hidden number, try again')  # Inform user their guess is too high
                continue
            elif user_number == number:
                print('You guessed it, congratulations!')  # Congratulate user for correct guess
                print('Would you like to play again?')  # Ask if user wants to play again
                consent_check(), number_range()  # Check user's consent and reset the game

# Farewell message
print('Thank you for playing the Number Guessing Game. See you again soon...')  # Farewell message
