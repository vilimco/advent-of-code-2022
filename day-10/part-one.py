input_file = open('input.txt', 'r')
input = [value.strip() for value in input_file.readlines()]

x = 1

cycle_number = 0
sum = 0


def run_cycle():
    global cycle_number, sum

    cycle_number = cycle_number + 1

    if (cycle_number - 20) % 40 == 0:
        signal_strength = x * cycle_number
        sum += signal_strength

    return


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


print("Sum", sum)
