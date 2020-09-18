test_data = input('Please enter the string:')

if test_data.isalpha():
    print('The strign is text only.')

elif test_data.isnumeric():
    print('The string is numbers only.')

elif test_data.isalnum():
    print('The string is mixed.')