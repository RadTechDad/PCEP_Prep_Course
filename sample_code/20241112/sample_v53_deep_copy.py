import copy 

my_list = [ 100, 40, 30, 50, 90, 60]

# List has 3 options
new_list = copy.deepcopy(my_list) # Most generic
new_list = my_list.copy()  # Varies
new_list = my_list[:] # Lists only 

my_set = { 100, 40, 30, 50, 90, 60}

# Set has 2 options
new_set = copy.deepcopy(my_set) # Most generic
new_set = my_set.copy() # Varies
new_set = set(my_set) # Create one from the original (Copy Constructor)

