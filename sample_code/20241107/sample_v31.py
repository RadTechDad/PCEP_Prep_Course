# start, stop, step 

# Start = 0 
# Stop = 10  -- Exclusive (Meaning the last value is not included)
# Step = 1
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

print(list(range(0, 10, 1)))

print(list(range(3, 10, 3))) # 3, 6, 9
print(list(range(3, 100, 10))) # 3, 13, 23, 33, 43, 53, 63, 73, 83, 93

# Step - defaults to 1
print(list(range(0, 10)))


# Start - defaults to 0, only if step is also default 
print(list(range(10)))

# (start, stop, step)
# (start, stop) - step defaults to 1
# (stop) - start defaults to 0, step defaults to 1
