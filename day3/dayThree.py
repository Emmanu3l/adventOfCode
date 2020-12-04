with open("input.txt") as file:
    lst = file.read().splitlines()


def count_trees(right, down):
    tree_count = 0
    column_count = 0
    i = 0
    while i < len(lst):
        if lst[i][column_count] == "#":
            tree_count += 1
        column_count = (column_count + right) % len(lst[i])
        i = i + down
    return tree_count


# part 1
# solution: 270
print(count_trees(3, 1))

# part 2
# solution 2122848000
print(count_trees(1, 1) * count_trees(3, 1) * count_trees(5, 1) * count_trees(7, 1) * count_trees(1, 2))
