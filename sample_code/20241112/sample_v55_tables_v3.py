NUM_ROWS = 4
NUM_COLS = 4
INIT = None 

# table = [] # dest
# for rowNum in range(NUM_ROWS): # loop
#     # row = [] # Dest 
#     # for colNum in range(NUM_COLS): # Loop
#     #     row.append(INIT)
#     #     #         ^    ^
#     #     #         |    |
#     #     #         ------
#     #     #         expression
#     table.append([INIT for colNum in range(NUM_COLS)])
#     #            ^                                  ^
#     #            |                                  |
#     #            ------------------------------------
#     #                       expression
table = [[rowNum*NUM_COLS + colNum for colNum in range(NUM_COLS)] for rowNum in range(NUM_ROWS)]

# print(table)
    
print("[")
for row in table:
    print("\t", row)
print("]")