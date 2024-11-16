fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']

user_input = input("Please enter a fruit: ")

# Sanitize the input
target = user_input.lower().strip()

print(user_input in fruits)
print(target in fruits)

# Manual Search
# found = False

# for fruit in fruits:
#     if fruit == target:
#         print("Found it!")
#         found = True
#         break

# if not found:
#     print("Not found!")
