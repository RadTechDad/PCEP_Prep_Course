my_list = [ 100, 40, 30, 50, 90, 60]

my_list_2 = my_list # link to the same object

del my_list

print(my_list_2) # Still valid 

print(my_list_2[:][2:3])