
value1 = 10
value2 = 23

#     False              True              False              False
if value1 > value2 and value1 % 2 == 0 or value2 % 2 == 0 and value1 > value2:
#                 False                or             False
#                                    False
    print("Success")
else:
    print("Error")

"""
Hi, 

I am practicing my order of operations can you setup some practice problems like this one:
```
value1 = 10
value2 = 23

if value1 > value2 and value1 % 2 == 0 or value2 % 2 == 0 and value1 > value2:
    print("Success")
else:
    print("Error")
```

Where I need to figure out which condition will run and it is dependent on the order of operations 
"""