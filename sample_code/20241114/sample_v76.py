def isInt(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def isFloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def isNumber(value): # Same as isFloat but shows using nested try/except
    try:
        int(value)
        return True
    except ValueError:
        try:
            float(value)
            return True
        except ValueError:
            return False    
    
user_input = input("Please enter a number: ")
while not isNumber(user_input):
    print("That was not a valid number!")
    user_input = input("Please enter a number: ")
print("Done!")