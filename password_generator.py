from random import *
import string


# Function to get password generation conditions from the user
def get_conditions():
    global chars
    print('Enter password generation conditions')
    digits_include = input('Include digits 0123456789? Enter + for yes or - for no:')
    if digits_include in '+':
        chars += string.digits
    lowercase_include = input('Include lowercase letters abcdefghijklmnopqrstuvwxyz? Enter + for yes or - for no: ')
    if lowercase_include in '+':
        chars += string.ascii_lowercase
    uppercase_include = input('Include uppercase letters ABCDEFGHIJKLMNOPQRSTUVWXYZ? Enter + for yes or - for no: ')
    if uppercase_include in '+':
        chars += string.ascii_uppercase
    symbols_include = input('Include symbols? Enter + for yes or - for no: ')
    if symbols_include in '+':
        chars += string.punctuation
    symbols_exclude = input('Exclude ambiguous symbols il1Lo0O? Enter + for yes or - for no: ')
    if symbols_exclude in '+':
        for char_to_remove in 'il1Lo0O':
            chars = chars.replace(char_to_remove, '')


# Function to generate passwords based on user-defined conditions
def password_generate():
    quantity = int(input("Enter the number of passwords to generate: "))
    length = int(input("Enter the length of one password: "))
    for i in range(quantity):
        print(''.join(sample(chars, length)))


flag = True
start_gen = input(
    'Welcome to the password generator! If you want to generate a password or several, enter "Yes" or "No": ')

# Check user's response to start or skip password generation
if start_gen.lower() in 'no':
    flag == False
    print('Thank you for using the password generator.')
else:
    while flag == True:
        chars = ''
        get_conditions()
        password_generate()
        answer = input('Do you want to continue password generation? Enter "Yes" or "No": ')
        # Check user's response to continue or end the password generation loop
        if answer.lower() in 'yes':
            flag == True
        else:
            flag == False
            print('Thank you for using the password generator.')
            break
