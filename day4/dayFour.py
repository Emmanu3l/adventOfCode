with open("input.txt") as file:
    lst = file.read().split("\n\n")

# part 1
# solution: 204
matches = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
validCount = 0
for passport in lst:
    if all(x in passport for x in matches):
        validCount += 1
print(validCount)

# part 2
# solution:

