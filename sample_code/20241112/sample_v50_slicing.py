alphabet = [
    #  0,   1,   2,   3,   4,   5,   6,   7,   8,   9,   10  
      'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 
    # -26  -25  -24  -23  -22  -21  -20  -19  -18  -17  -16

    #  11,  12,  13,  14,  15,  16,  17,  18,  19,  20,  21
       'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
    # -15  -14  -13  -12  -11  -10  -9   -8   -7   -6   -5

    # 22    23  24    25    
      'W', 'X', 'Y', 'Z'
    # -4   -3   -2   -1
]

# Whole sequence (Forwards) -- Positive Step
# start : stop : step
# print(alphabet[:]) # Using all defaults , start = 0, end = len(alphabet), step = 1
# print(alphabet[::]) # Using all defaults , start = 0, end = len(alphabet), step = 1
# print(alphabet[0:len(alphabet):1]) # Fully specified
# print(alphabet[0:len(alphabet)]) # default step = 1
# print(alphabet[0:]) # default step = 1, stop = len(alphabet)
# print(alphabet[:len(alphabet)]) # default step = 1, start = 0


# Whole sequence (Backwards) -- Negative Step
# print(alphabet[::-1]) # Using negative defaults , start = -1, end = (-len(alphabet) - 1)


# Subset Selection (Forwards) -- Positive Step
print(alphabet[0:5]) # A, B, C, D, E
print(alphabet[-26:-21]) # A, B, C, D, E

# Subset Selection (Backwards) -- Negative Step
print(alphabet[4::-1]) # E, D, C, B, A
print(alphabet[-22::-1]) # E, D, C, B, A
