input_file = open('input.txt', 'r')
input = input_file.readlines()

elf_calories = 0
elfs = []

# Strips the newline character
for rawLine in input:
    line = rawLine.strip()
    if line != "":
        elf_calories += int(line)
        continue

    elfs.append(elf_calories)
    elf_calories = 0

elfs.append(elf_calories)
elfs.sort(reverse=True)

print("Max calories: ", elfs[0] + elfs[1] + elfs[2])
