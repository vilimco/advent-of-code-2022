input_file = open('input.txt', 'r')
input = [value.strip() for value in input_file.readlines()]

head_x = 0
head_y = 0
number_of_tails = 9
tails = []
for i in range(0, number_of_tails):
    tails.append([0, 0])


def move(direction):
    global head_x, head_y, tails
    if direction == "R":
        head_x += 1
    if direction == "L":
        head_x -= 1
    if direction == "U":
        head_y += 1
    if direction == "D":
        head_y -= 1

    shead_x = head_x
    shead_y = head_y

    for i in range(0, number_of_tails):
        x_distance = abs(shead_x - tails[i][0])
        y_distance = abs(shead_y - tails[i][1])
        tail_distance = x_distance + y_distance

        # If overlap, neighbour or diagonal neighbour, no change
        if tail_distance <= 1 or (x_distance == y_distance and tail_distance == 2):
            return

        if tail_distance >= 2:
            tails[i][0] = shead_x + round((tails[i][0] - shead_x) / 2)
            tails[i][1] = shead_y + round((tails[i][1] - shead_y) / 2)

        shead_x = tails[i][0]
        shead_y = tails[i][1]


def get_tail_pos():
    global tails
    return str(tails[8][0]) + "," + str(tails[8][1])


visited = set()
visited.add(get_tail_pos())
for line in input:
    direction, rawAmount = line.split(" ")

    for i in range(0, int(rawAmount)):
        move(direction)

        visited.add(get_tail_pos())

print("Visited", len(visited))
