with open("input.txt") as file:
    lst = file.readlines()

validCount = 0
validCountTwo = 0

# part 1
# solution: 515
for password in lst:
    parts = password.split(" ")
    lowest, highest = parts[0].split("-")
    character = parts[1][:-1]
    string = parts[2]
    if int(lowest) <= string.count(character) <= int(highest):
        validCount += 1
print(validCount)
# 515

# part two
# solution 711
for password in lst:
    parts = password.split(" ")
    lowest, highest = parts[0].split("-")
    newLow = int(lowest) - 1
    newHigh = int(highest) - 1
    character = parts[1][:-1]
    string = parts[2]
    if (string[newLow] == character) != (string[newHigh] == character):
        validCountTwo += 1
print(validCountTwo)
