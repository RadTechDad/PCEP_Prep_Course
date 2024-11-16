breakFlag = False
for counter in []: # range(2,1) # range(0) -- counter not created
    print(f"Counter: {counter}")
    counter += 1
    if counter == 2:
        print("Breaking!")
        breakFlag = True
        break
else:
    print(f"Done {counter}!")

print(f"The End {counter}!")

if not breakFlag:
    print("No break statement was executed!")