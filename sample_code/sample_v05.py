# Absoute Path
# testFile = open("/Users/user/Developer/Python/test_data/testFile1.csv", "r")
# testFile = open("/Users/user/Developer/Python/test_data/mockaroo.csv", "r")

# Relative Path 
# testFile = open("day_02/test_data/testFile1.csv", "r")
testFile = open("day_02/test_data/mockaroo.csv", "r")

for line in testFile:
    print(line)
