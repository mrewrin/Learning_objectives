from random import *

# List of possible answers from the Magic 8-ball
answers = ["It is certain", "It is decidedly so", "Without a doubt", "Yes, definitely",
           "You may rely on it", "As I see it, yes", "Most likely", "Outlook good",
           "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later",
           "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
           "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good",
           "Very doubtful"]

# Welcome message and asking for the user's name
print('Hello World, I am the magic 8-ball, and I know the answer to any of your questions.')
print('What is your name?')
name = input()
print(f'Hello, {name}!')

# Asking if the user wants to know the future
print(f'Do you want to know the future, {name}? Enter "YES" or "NO"')
answer = input()

# Responding based on the user's choice
if answer.lower() == 'no':
    print('Well, then continue living in ignorance!')
if answer.lower() == 'yes':
    while True:
        # Asking the user to input a question
        print('Ask the unknown')
        question = input()
        # Providing a random answer from the Magic 8-ball
        print(choice(answers))
        # Asking if the user wants to ask another question
        print(f'Do you want to ask another question? Enter "YES" or "NO":')
        yes_or_no = input()
        # Checking the user's response to continue or end the loop
        if yes_or_no.lower() == 'yes':
            continue
        elif yes_or_no.lower() == 'no':
            print('Come back if you have any more questions!')
            break
        else:
            # Handling incorrect input from the user
            print('Didn\'t get you, try again:')
