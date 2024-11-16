# Goal is to implement Bubble Sort

# Toolbox:
#   while loop 
#   for loop in the while loop 
#   boolean or flag for tracking the while loop status
#   if - comparison 
#   swap operation

#         0   1  2  3  4  len(values) => 5
values = [8, 10, 6, 2, 4]

print("Original Values: ", values)

isNotSorted = True
while isNotSorted:

    swapOccured = False
    # Runs through every element - this for loop is completing a pass
    for index in range(len(values) - 1):
        # print(f"Index: {index}, values[index]: {values[index]}")
        # Compares the neighboring elements
        if values[index] > values[index + 1]: # index + 1 < len(values) and 
            # Swaps if the current element is greater than the next element
            values[index], values[index+1] = values[index+1], values[index]
            swapOccured = True            

    if swapOccured == False:
        isNotSorted = False

    print(values)