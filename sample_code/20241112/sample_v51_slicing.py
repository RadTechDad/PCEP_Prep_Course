alphabet = [
    #  0,   1,   2,   3,   4,   5,   6,   7,   8,   9,   10  
      'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 
    # -26  -25  -24  -23  -22  -21  -20  -19  -18  -17  -16

    #  11,  12,  13,  14,  15,  16,  17,  18,  19,  20,  21
       'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
    # -15  -14  -13  -12  -11  -10  -9   -8   -7   -6   -5

    # 22    23  24   25    
      'W', 'X', 'Y', 'Z'
    # -4   -3   -2   -1
]

# Positive Step
print(alphabet[15 : 20]) # --> ['P', 'Q', 'R', 'S', 'T']
print(alphabet[20 : 15]) # --> []
print(alphabet[-1 : 3 ]) # --> []
print(alphabet[ 22 : 1000]) # --> ['W', 'X', 'Y', 'Z']

# Negative Step :-1
print(alphabet[15 : 20 : -1]) # --> []
print(alphabet[20 : 15 : -1]) # --> [ 'U', 'T', 'S', 'R', 'Q']