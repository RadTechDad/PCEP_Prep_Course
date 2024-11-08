sample_tuple = (5,1)
print(f"type(sample_tuple): {type(sample_tuple)}, sample_tuple: {sample_tuple}")

print(sample_tuple * 3)

sample_tuple_2 = (5, 6, 7)

new_list = list(sample_tuple_2)

new_list[1] = 8
print(sample_tuple_2)
print(new_list)