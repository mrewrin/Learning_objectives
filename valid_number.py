# The program checks if the entered string is a valid phone number.
# A string is considered a valid phone number if it has the format:
# abc-def-hijk or 7-abc-def-hijk,
# where a, b, c, d, e, f, h, i, j, k are digits from 0 to 9.

# Take input from the user
string = input()

# Remove '-' characters from the input string
exam_1 = string.replace('-', '')

# Check if the resulting string consists only of digits
if exam_1.isdigit() == False:
    print('NO')  # If not, print 'NO'
else:
    exam_2 = string.split('-')  # Split the string at '-' characters
    exam_list = []
    # Iterate through the resulting list to get the lengths of each substring
    for i in exam_2:
        exam_list.append(len(i))
    # Check if the lengths of substrings match the expected pattern
    if exam_list == [3, 3, 4] or ([1, 3, 3, 4] and exam_2[0] == '7'):
        print('YES')  # If yes, print 'YES'
    else:
        print('NO')  # If not, print 'NO'
