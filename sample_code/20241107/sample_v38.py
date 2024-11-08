fruits = ["apple", "banana", "cherry"]

user_input = input("Enter a fruit: ")

for fruit in fruits:
    print("Checking: ", fruit)
    if fruit == user_input:
        print(f"{user_input} found!")
        break
