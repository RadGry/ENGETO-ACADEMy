# WELCOME header

print('='*40)
print('Welcome to DESTINADO,\nplace where people plan their trips')
print('='*40)

# Destination Cities + Prices

print('We can offer you following destinations:')
print('-'*40)
print('''
    1 - Prague  |   1000
    2 - Wein    |   1100
    3 - Brno    |   2000
    4 - Svitavy |   1500
    5 - Zlin    |   2300
    6 - Ostrava |   3400
''')

# Destination Selection (check if there is a way to replace this with dictionary?)

selection = int(input('Please enter the number of the destination to select:'))

DESTINATIONS = ['Prague', 'Wein', 'Brno', 'Svitavy', 'Zlin', 'Ostrava']
PRICES = ['1000', '1100', '2000', '1500', '2300', '3400']

destination_chosen = DESTINATIONS[selection - 1]
price_chosen = PRICES[selection - 1]

# zadani podmínky slevy

if selection is 4 or 6:
    print('Lucky you! You have just earned 25% discount for your destination - ' + destination_chosen)
    price_chosen = price_chosen * 0,75


print('='*40)
print('REGISTRATION')
print('-'*40)
print('In order to complete your reservations, please share few detaisl with us:')
print('-'*40)

# is it better to assign object types in separate section?
# name = str()
# last_name = str()
# yob = int()
# email = str()
# password = str()


name = input('NAME:  ')
print('='*40)  # spacing
last_name = input('LAST NAME:  ')
print('='*40)  # spacing
yob = input('YEAR OF BIRTH:  ')
print('='*40)  # spacing
email = input('EMAIL:  ')
print('='*40)  # spacing
password = input('PASSWORD:  ')

# Conditions
from datetime import date
current_date = date.today()
age = current_date.year - int(yob)

if age < 15:
    print('You must be 15 years old to use our services')

elif '@' not in email:
    print('Email is not correct')

elif len(password) < 8:
    print('The password is the short. It needs to have 8 characters')

elif password[0].isnumeric:
    print('The password can not start with number')

elif password[-1].isnumeric:
    print('The password can not end with number')

elif password.isalpha() or password.isnumeric() or not password.isalnum():
    print('Password need to contain letters and numbers')

else:

    print('Thank you ' + name)
    print('We confirm you reservation in ' + destination_chosen)
    print('Your price is ' + price_chosen)