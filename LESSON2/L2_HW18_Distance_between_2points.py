import math

AX = int(input('Bod A - zadejte souřadnici X: '))

AY = int(input('Bod A - zadejte souřadnici Y: '))

BX = int(input('Bod B - zadejte souřadnici X: '))

BY = int(input('Bod B - zadejte souřadnici Y: '))

# distance calculation

distance_fund = float((AX - BX)*(AY - BY))

distance = round(math.sqrt(abs(distance_fund)), 2)

print(distance_fund)
print(distance)