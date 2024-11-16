
# In-place Operation
def add_ten_to_each_entry(target_list):
    for index in range(len(target_list)):
        target_list[index] += 10

# Assmptions:
# 1. target_list supports the len() function
# 2. target_list supports the [] operator
# 3. the entries in target_list support the += operator with and integer

my_list = [1, 2, 3, 4, 5] #["Hello"] #5 #
print("Before:", my_list)
add_ten_to_each_entry(my_list) # Relies on the shallow copy otherwise no change
print("After:", my_list)