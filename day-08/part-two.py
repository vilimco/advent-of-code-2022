input_file = open('input.txt', 'r')
input = [value.strip() for value in input_file.readlines()]

trees = []


def get_visibility_index(forest, x, y):
    height = len(forest)
    width = len(forest[0])
    tree = forest[y][x]

    north_score = 0
    for i in range(y - 1, -1, -1):
        north_score += 1
        if forest[i][x] >= tree:
            break

    south_score = 0
    for i in range(y + 1, height):
        south_score += 1
        if forest[i][x] >= tree:
            break

    west_score = 0
    for i in range(x - 1, -1, -1):
        west_score += 1
        if forest[y][i] >= tree:
            break

    east_score = 0
    for i in range(x + 1, width):
        east_score += 1
        if forest[y][i] >= tree:
            break

    return south_score * north_score * west_score * east_score


for line in input:
    tree_row = [int(val) for val in list(line)]
    trees.append(tree_row)

forrest_height = len(trees)
forrest_width = len(trees[0])

visible_trees = 2 * (forrest_width + forrest_height) - 4

max_score = 0
for coordY in range(0, forrest_height):
    for coordX in range(0, forrest_width):
        score = get_visibility_index(trees, coordX, coordY)
        if score > max_score:
            max_score = score

print("Max score", max_score)
