import decimal

# Pass number in as a string, not a float
# If a float is passed in, precision will be locked
# Decimals hold higher precision than floats
newVariable = decimal.Decimal('0.1')
print(type(newVariable))
