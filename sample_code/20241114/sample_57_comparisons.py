# print(5==5.0) # True
# print(3.14==3.15) # False

my_list = [1, 2, 3, 4, 5, 3.14]

# print(5.0 in my_list) # True
# print(3.15 in my_list) # False

user_input = input("Please enter a number: ")

print(float(user_input) in my_list)
print(float(user_input) not in my_list)