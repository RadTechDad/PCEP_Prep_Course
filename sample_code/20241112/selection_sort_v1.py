# Goal: Implement Selection Sort

# Toolbox:
#    while loop (determines how many passes we need)
#        for loop in the while loop (performs the pass)
#            if - comparison (check whether or not this is the smallest value)

# NOTE: we need to adjust the starting location on each iteration
#   - fos - first open slot
#   - smlst - index of the smallest value

#         0   1  2  3  4  len(values) => 5
values = [8, 10, 6, 2, 4]

print("Original Values: ", values)

first_open_slot = 0
while first_open_slot < len(values):
    # Runs once per pass
    index_of_the_smallest = first_open_slot
    # NOTE: This is giving us a dynamic starting point
    for index in range(first_open_slot, len(values)):
        # Runs as part of the pass (once for each value in the list)
        if values[index_of_the_smallest] > values[index]:
            index_of_the_smallest = index

    # Also once per pass
    # Swap the smallest value with the first open slot
    values[first_open_slot], values[index_of_the_smallest] = values[index_of_the_smallest], values[first_open_slot]

    first_open_slot += 1

    print(values)

print(values)