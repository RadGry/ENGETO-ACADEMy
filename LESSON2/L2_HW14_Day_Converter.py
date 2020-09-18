# vytvoření seznam dní

days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

r = range (1,8)

day_number = input('Please enter the number of the day of the week (1-7): ')

if not day_number:
    print('No input provided.')

elif not day_number.isnumeric():
    print('Enter only numbers.')

else:
    day_number = int(day_number)

if int(day_number) not in r:
    print('Enter only numbers between 1-7.')

else:
    day_selection = int(day_number) - 1
    print(days[day_selection])