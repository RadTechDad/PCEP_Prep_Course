dictionary = {
    # key -> value
    # word -> definition
    "apple" : "A red fruit.",
    "banana" : "A yellow fruit.",
}

for key, value in dictionary.items():
    print(f"Key: {key}, Value: {value}")

# print(dictionary)

# # Accessing a value
# print(dictionary["apple"])

# # Days of the week
# days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# stores = ["Electronics", "Grocery", "Clothing"]

numCustomers = {
    "Monday" : {
        "Electronics" : 100,
        "Grocery" : 200,
        "Clothing" : 300,
    },
    "Tuesday" : {
        "Electronics" : 150,
        "Grocery" : 250,
        "Clothing" : 350,
    },
}

# # print(numCustomers['Monday']['Electronics'])

# # for day in numCustomers:
# #     print(day)
# #     print(numCustomers[day])
# #     for store in numCustomers[day]:
# #         print(store)

# for key, value in numCustomers.items():
#     print(f"Layer 1: Key: {key}, Value: {value}")
#     for store, customers in value.items():
#         print(f"\tLayer 2: Key: {store}, Value: {customers}")
#         print(numCustomers[key][store])