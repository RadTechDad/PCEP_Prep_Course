user_input = int(input("Enter a number: "))

if user_input % 2 == 0:
    print("The number is even")
elif user_input == 101:
    print("You guessed the magic number!")
else:
    print("The number is odd")