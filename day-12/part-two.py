input_file = open('input.txt', 'r')
input = [value.strip() for value in input_file.readlines()]

height = len(input)
width = len(input[0])

terrain = [list(row) for row in input]

end = [0, 0]

for y in range(0, height):
    for x in range(0, width):
        if terrain[y][x] == "E":
            end = [x, y]


def get_key(x, y):
    return str(x) + "-" + str(y)


def get_elevation(x, y):
    val = terrain[y][x]
    if val == "S":
        val = "a"
    if val == "E":
        val = "z"
    return ord(val)


def get_path(start):
    end_key = get_key(end[0], end[1])
    start_key = get_key(start[0], start[1])

    queue = [start]
    visited = {}
    length = {}
    length[start_key] = 0

    while len(queue) > 0:
        x, y = queue.pop(0)
        key = get_key(x, y)

        if key in visited:
            continue

        visited[key] = True

        new_length = length[key] + 1

        if key == end_key:
            length[end_key] = new_length
            break

        elevation = get_elevation(x, y)

        # move left
        if x > 0:
            left_key = get_key(x - 1, y)
            left_elevation = get_elevation(x - 1, y)
            if left_key not in visited and left_elevation - elevation <= 1:
                queue.append([x - 1, y])
                length[left_key] = new_length

        # move left
        if x < width - 1:
            right_key = get_key(x + 1, y)
            right_elevation = get_elevation(x + 1, y)
            if right_key not in visited and right_elevation - elevation <= 1:
                queue.append([x + 1, y])
                length[right_key] = new_length
        # move up
        if y > 0:
            up_key = get_key(x, y - 1)
            up_elevation = get_elevation(x, y - 1)
            if up_key not in visited and up_elevation - elevation <= 1:
                queue.append([x, y - 1])
                length[up_key] = new_length
        # move down
        if y < height - 1:
            down_key = get_key(x, y + 1)
            down_elevation = get_elevation(x, y + 1)
            if down_key not in visited and down_elevation - elevation <= 1:
                queue.append([x, y + 1])
                length[down_key] = new_length

    if end_key not in length:
        return height * width

    return length[end_key] - 1


shortest_path = height * width


for y in range(0, height):
    for x in range(0, width):
        if terrain[y][x] != "a":
            continue
        length = get_path([x, y])
        if length < shortest_path:
            shortest_path = length

print(shortest_path)
