
# In-place Operation
def set_index_2_to_5(target_list):                      # First line to run
    print("(2) my_list Before:", my_list)               #   --> 5th line to run
    print("(3) target_list Before:", target_list)       #   --> 6th line to run
    target_list[2] = 5                                  #   --> 7th line to run
    print("(4) my_list After:", my_list)                #   --> 8th line to run
    print("(5) target_list After:", target_list)        #   --> 9th line to run

my_list = [1, 2, 3, 4, 5]                              # Second line to run
print("(1) Before:", my_list)                          # Third line to run
set_index_2_to_5(my_list)                              # Fourth line to run
print("(6) After:", my_list)                           # Tenth line to run