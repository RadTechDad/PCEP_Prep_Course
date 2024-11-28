import re as regex

# Exercise 24 - Let's explore finding the max
###############################################################################

print('\n# -=[ Exercise 24 ]=- ############################################\n')
highest_value = 0
list_of_values = []

while True:
    value = input("Enter a value <= 0 to quit: ")

    if value == "":
        continue

    # Determine if the value given is an int or float
    if regex.search(r'\.', value):
        try:
            value = float(value)
        except ValueError:
            print("That was not a valid number!")
            continue
    else:
        try:
            value = int(value)
        except ValueError:
            print("That was not a valid number!")
            continue

    if value < 0:
        break
    elif value == 0 and len(list_of_values) == 0:
        print("No Numbers Input ?!?")
        break
    elif value == 0 and len(list_of_values) > 0:
        print(f"The list of values given were: {list_of_values}")
        print(f"The largest value is {highest_value:.1f}")
        break
    else:
        list_of_values.append(value)

        if value > highest_value:
            highest_value = value


# Exercise 28 - Check if Python is in a String
###############################################################################

print('\n# -=[ Exercise 28 ]=- ############################################\n')

# Ask the user for a string then report whether or not the word "python"
# is in the string.

user_string = input("Enter a string: ").strip()
sanitized_user_string = user_string.lower()

if "python" in sanitized_user_string:
    print(f'"Python" is in "{user_string}".')
else:
    print(f'"Python" is not in "{user_string}".')
