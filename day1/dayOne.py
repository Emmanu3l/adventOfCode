import itertools

with open("input.txt") as file:
    lst = [int(x) for x in file.readlines()]

# part 1
# solution: 1016964
for a, b in itertools.combinations(lst, 2):
    if a + b == 2020:
        print(a * b)
# part 1
# solution: 182588480
for a, b, c in itertools.combinations(lst, 3):
    if a + b + c == 2020:
        print(a * b * c)
