# ask the user of age

age = int(input('How old are you:'))

# calculate and print YOB

from datetime import date
current_date = date.today()
YOB = current_date.year - int(age)
print('You were probably born in: ', + YOB)