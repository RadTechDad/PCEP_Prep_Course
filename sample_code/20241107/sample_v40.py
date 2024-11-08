fruits = ["apple", "banana", "cherry"]

user_input = input("Enter a fruit: ")

index = 0
while index < len(fruits):
    fruit = fruits[index]
    print("Checking: ", fruit)
    if fruit == user_input:
        print(f"{user_input} found!")
        break
    index += 1