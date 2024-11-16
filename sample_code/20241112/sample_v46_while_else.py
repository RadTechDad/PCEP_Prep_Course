
counter = 0
while counter < 2:
    print("*", end="")
    if counter % 2 == 0:
        print("!", end="")
    counter += 1
    print("@", end="")
else:
    print("^", end="")

print("-", end="")
print()

# counter | print("*") | counter % 2 == 0 | print("!") |counter += 1 |  print("@") |
# ----------------------------------------------------------------------------------
#   0     |    *       |       True       |     !      |      1      |     @   
#   1     |    *       |       False      |            |      2      |     @
# Else -> ^
# -

# Final Output: *!@*@^-
