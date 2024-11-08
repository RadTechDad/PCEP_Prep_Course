
#  0,  1,  2,  3,  4,  5,  6,  7,  8, 9,  10  < --- Index
# 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
numbers = list(range(10, 21)) 

# Double the even numbers
for index in range(len(numbers)):
    print(f"Index: {index}, numbers[index]: {numbers[index]}")
    # Is it odd? 
    if index % 2 != 0:
        # If yes skip it
        continue    
    # Only even values will reach this point and be doubled
    numbers[index] = numbers[index] * 2

    # if number % 2 == 0: # Is it an even number?
    #     # If yes double it 
    #     numbers[number] = numbers[number] * 2

print(numbers) # 0, 1, 4, 3, 8, 5, 12, 7, 16, 9, 20