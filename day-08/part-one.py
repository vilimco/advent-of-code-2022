input_file = open('input.txt', 'r')
input = [value.strip() for value in input_file.readlines()]

trees = []


def is_visible(forest, x, y):
    height = len(forest)
    width = len(forest[0])
    tree = forest[y][x]

    visible_to_north = True
    for i in range(0, y):
        if forest[i][x] >= tree:
            visible_to_north = False
            break

    if visible_to_north:
        return True

    visible_to_south = True
    for i in range(y + 1, height):
        if forest[i][x] >= tree:
            visible_to_south = False
            break

    if visible_to_south:
        return True

    visible_to_west = True
    for i in range(0, x):
        if forest[y][i] >= tree:
            visible_to_west = False
            break

    if visible_to_west:
        return True

    visible_to_east = True
    for i in range(x + 1, width):
        if forest[y][i] >= tree:
            visible_to_east = False
            break

    if visible_to_east:
        return True

    return False


for line in input:
    tree_row = [int(val) for val in list(line)]
    trees.append(tree_row)

forrest_height = len(trees)
forrest_width = len(trees[0])
print(forrest_width, forrest_height)

visible_trees = 2 * (forrest_width + forrest_height) - 4

for coordY in range(1, forrest_height - 1):
    for coordX in range(1, forrest_width - 1):
        if is_visible(trees, coordX, coordY):
            visible_trees += 1

print("Visible trees", visible_trees)

