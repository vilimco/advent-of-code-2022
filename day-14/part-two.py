import json

input_file = open('input.txt', 'r')
input = [value.strip() for value in input_file.readlines()]

cave = {}
floor_level = 0
def get_key(x, y):
    return str(x) + "-" + str(y)


for line in input:
    paths = [list(map(int, value.split(","))) for value in line.split(" -> ")]

    start_x, start_y = paths[0]

    for i in range(1, len(paths)):
        end_x, end_y = paths[i]

        for x in range(min(start_x, end_x), max(start_x, end_x) + 1):
            for y in range(min(start_y, end_y), max(start_y, end_y) + 1):
                cave[get_key(x, y)] = "#"

        start_x = end_x
        start_y = end_y

        floor_level = max(floor_level, end_y)

floor_level += 2

start_key = get_key(500, 0)

sand_start = [500, 0]
sand_x, sand_y = sand_start
sands = 0
while(True):

    if sand_y + 1 == floor_level:
        current_key = get_key(sand_x, sand_y)
        cave[current_key] = "o"
        sands += 1
        sand_x, sand_y = sand_start

    bottom_key = get_key(sand_x, sand_y + 1)
    if bottom_key not in cave:
        sand_y += 1
        continue

    left_key = get_key(sand_x - 1, sand_y + 1)
    if left_key not in cave:
        sand_x -= 1
        sand_y += 1
        continue

    right_key = get_key(sand_x + 1, sand_y + 1)
    if right_key not in cave:
        sand_x += 1
        sand_y += 1
        continue

    current_key = get_key(sand_x, sand_y)
    cave[current_key] = "o"
    sands += 1
    sand_x, sand_y = sand_start

    if current_key == start_key:
        break


print(sands)
