
magic_number = 100

print("Can you guess the magic number? How many tries will it take?")

tryCount = 0

user_input = int(input("Enter a number: "))

if user_input == magic_number:
    print("You guessed the magic number!")
elif user_input < magic_number:
    print("Your guess is too low")
else:   
    print("Your guess is too high")

tryCount += 1