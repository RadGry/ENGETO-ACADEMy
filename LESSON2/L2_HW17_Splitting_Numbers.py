# input

number1 = input('Please give me the number: ')

if number1 == '':
    print('No input provided')

elif len(number1) % 2 == 0:

    middle1 = len(number1) // 2

    half1 = int(number1[:middle1])
    half2 = int(number1[middle1:])

    if half1 % 2 == 0 and half2 % 2 == 0:
        print('Success')

    elif half1 % 2 == 0:
        print('First')

    elif half2 % 2 == 0:
        print('Second')

    else:
        print('Neither')


