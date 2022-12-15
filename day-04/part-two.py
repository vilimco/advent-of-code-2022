input_file = open('input.txt', 'r')
input = input_file.readlines()

def split_range(line):
    return list(map(int, line.split(sep="-")))

overlaps = 0
for rawLine in input:
    line = rawLine.strip()
    if line == "":
        continue

    tasks = line.split(sep=",")
    elf1, elf2 = list(map(split_range, tasks))

    if elf1[1] >= elf2[0] and elf1[0] <= elf2[1]:
        overlaps += 1

print("Overlaps:", overlaps)





