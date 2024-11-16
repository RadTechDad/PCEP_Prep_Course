dictionary = {
    # key -> value
    # word -> definition
    "apple" : "A red fruit.",
    "banana" : "A yellow fruit.",
}

# # Direct
# for key in dictionary:
#     print(f"Key: {key}, Value: {dictionary[key]}")


# # Keys
# for key in dictionary.keys():
#     print(f"Key: {key}, Value: {dictionary[key]}")

# Items - Key, Value
for keyValuePair in dictionary.items():
    print(keyValuePair)
    key, value = keyValuePair
    print(f"Key: {key}, Value: {value}")
    print(f"Alternative Print Key: {keyValuePair[0]}, Value: {keyValuePair[1]}")

# for key, value in dictionary.items():
#     print(f"Key: {key}, Value: {value}")

# # Values
# for value in dictionary.values():
#     # If you use values, cannot get the key
#     print(f"Value: {value}")