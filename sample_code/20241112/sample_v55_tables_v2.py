NUM_ROWS = 4
NUM_COLS = 4
INIT = None 

table = []
for rowNum in range(NUM_ROWS):
    # row = [] # Dest 
    # for colNum in range(NUM_COLS): # Loop
    #     row.append(INIT)
    #     #         ^    ^
    #     #         |    |
    #     #         ------
    #     #         expression
    row = [INIT for colNum in range(NUM_COLS)]
    table.append(row)

# print(table)
    
print("[")
for row in table:
    print("\t", row)
print("]")