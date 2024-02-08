# Function declaration
def number_to_words(num):
    # Lists to store words representing numbers
    list_word_1 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    list_word_2 = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
                   'nineteen']
    list_word_3 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    # Check if the input number is within the range of 1 to 99
    if 1 <= num <= 99:
        # For numbers less than 10
        if num // 10 == 0:
            return list_word_1[num - 1]
        # For numbers between 10 and 19
        elif num // 10 == 1:
            return list_word_2[num % 10]
        # For numbers in the range of 20 to 99
        elif num % 10 == 0:
            return list_word_3[(num // 10) - 2]
        # For numbers in the range of 21 to 99, excluding multiples of 10
        else:
            return list_word_3[(num // 10) - 2] + ' ' + list_word_1[(num % 10) - 1]


# Read the input number
n = int(input())

# Call the function and print the result
print(number_to_words(n))
