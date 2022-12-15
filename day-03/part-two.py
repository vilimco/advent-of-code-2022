input_file = open('input.txt', 'r')
input = input_file.readlines()

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


sum = 0

for i in range(0, len(input), 3):
    rucksack1 = input[i].strip()
    if rucksack1 == "":
        continue

    rucksack2 = input[i + 1].strip()
    rucksack3 = input[i + 2].strip()

    overlap = intersection(intersection(rucksack1, rucksack2), rucksack3)[0]
    match = ord(overlap)

    if match > 96:
        value = match - 96
    else:
        value = match - 65 + 27

    sum += value


print("Sum:", sum)
