from math import ceil

input_file = open('input.txt', 'r')
input = input_file.readlines()

break_index = 0
for line in input:
    if line.strip() == "":
        break
    break_index += 1

number_of_columns = ceil(len(input[break_index - 1])/4.0)

columns = []
for i in range(0, number_of_columns):
    columns.append([])

for i in range(0, break_index - 1):
    line = input[i]
    for c in range(0, number_of_columns):
        idx = c * 4 + 1
        if idx < len(line) and line[idx] != " ":
            columns[c].insert(0, line[idx])


for i in range(break_index + 1, len(input)):
    line = input[i].strip()

    _, move_amount, _, from_col, _, to_col = line.split(sep=" ")
    move_amount, from_col, to_col = list(map(int, [move_amount, from_col, to_col]))

    for j in range(0, move_amount):
        if len(columns[from_col - 1]) == 0:
            continue

        val = columns[from_col - 1].pop()
        columns[to_col - 1].append(val)


output = ""
for column in columns:
    output += column.pop()

print(output)


