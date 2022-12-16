input_file = open('input.txt', 'r')
input = [value.strip() for value in input_file.readlines()]

x = 1

cycle_number = 0
drawing = []
for i in range(0, 6):
    row = []
    for j in range(0, 40):
        row.append("")
    drawing.append(row)


def run_cycle():
    global cycle_number, drawing

    symbol = "."
    row = cycle_number // 40
    col = cycle_number % 40

    if abs(col - x) <= 1:
        symbol = "#"

    drawing[row][col] = symbol

    cycle_number = cycle_number + 1


for line in input:
    values = line.split(" ")
    cmd = values[0]

    if cmd == "noop":
        run_cycle()
    elif cmd == "addx":
        val = int(values[1])

        run_cycle()
        run_cycle()

        x += val


for row in drawing:
    print("".join(row))

