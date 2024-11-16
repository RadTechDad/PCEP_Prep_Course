NUM_ROWS = 2
NUM_COLS = 5
INIT = None 

table = []
for rowNum in range(NUM_ROWS):
    row = []
    for colNum in range(NUM_COLS):
        row.append(INIT)
    table.append(row)

# print(table)
    
print("[")
for row in table:
    print("\t", row)
print("]")