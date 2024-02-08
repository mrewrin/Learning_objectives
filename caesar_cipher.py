n = input()  # Get a string from the user.
# Remove punctuation marks and symbols that will not be considered during encryption.
s = n
for j in n:
    if j in '*,.!@"-':
        s = s.replace(j, '')
# Create a list `g` that contains the lengths of words from the string as numbers.
g = [len(i) for i in s.split()]
# Initialize variables for encryption.
count = 0
word_new = ''
# Iterate over each character in the original string `n`.
for d in n:
    number = ord(d)  # Get the numeric value of the character in Unicode encoding.

    if d == ' ':  # If the character is a space, increase the counter and add it to the result.
        count += 1
        word_new += chr(number)
    elif 65 <= number <= 90:  # If the character is an uppercase letter (A-Z), perform encryption.
        number += g[count]
        if number > 90:  # If the result goes beyond A-Z, perform a cyclic shift.
            number = number - 26
            word_new += chr(number)
        else:
            word_new += chr(number)
    elif 97 <= number <= 122:  # If the character is a lowercase letter (a-z), perform encryption.
        number += g[count]
        if number > 122:  # If the result goes beyond a-z, perform a cyclic shift.
            number = number - 26
            word_new += chr(number)
        else:
            word_new += chr(number)
    else:
        word_new += chr(number)  # If the character is not a letter, add it unchanged.

print(word_new)  # Print the decrypted string.
