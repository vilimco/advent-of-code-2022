input_file = open('input.txt', 'r')
input = [value.strip() for value in input_file.readlines()]

head_x = 0
head_y = 0
tail_x = 0
tail_y = 0


def move(direction):
    global head_x, head_y, tail_x, tail_y
    if direction == "R":
        head_x += 1
    if direction == "L":
        head_x -= 1
    if direction == "U":
        head_y += 1
    if direction == "D":
        head_y -= 1

    x_distance = abs(head_x - tail_x)
    y_distance = abs(head_y - tail_y)
    tail_distance = x_distance + y_distance

    # If overlap, neighbour or diagonal neighbour, no change
    if tail_distance <= 1 or (x_distance == y_distance and tail_distance == 2):
        return

    if tail_distance >= 2:
        tail_x = head_x + round((tail_x - head_x) / 2)
        tail_y = head_y + round((tail_y - head_y) / 2)


def get_tail_pos():
    global tail_x, tail_y
    return str(tail_x) + "," + str(tail_y)


visited = set()
visited.add(get_tail_pos())
for line in input:
    direction, rawAmount = line.split(" ")
    for i in range(0, int(rawAmount)):
        move(direction)
        visited.add(get_tail_pos())

print("Visited", len(visited))
