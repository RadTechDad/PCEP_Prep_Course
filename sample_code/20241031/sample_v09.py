from decimal import Decimal

# Pass number in as a string, not a float
# If a float is passed in, precision will be locked
# Decimals hold higher precision than floats
newVariable = Decimal('0.1')
print(type(newVariable))
