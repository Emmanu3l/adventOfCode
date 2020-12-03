with open("input.txt") as file:
    lst = [x for x in file.readlines()]

treeCount = 0
columnCount = 0

for i in range(len(lst)):
    if lst[i][columnCount] == "#":
        treeCount += 1
    columnCount = (columnCount + 3) % len(lst[i])
print(treeCount)
