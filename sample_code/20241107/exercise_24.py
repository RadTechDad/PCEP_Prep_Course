user=float(input("Enter a value <= 0 to quit :"))
largest=user
k= False

while user > 0:
    if largest < user:
        largest = user
        k=True
user=float(input("Enter a value <= 0 to quit :"))

if(k):
    print("The largest value is", largest)
else:
    print("No Numbers Input ?!?")