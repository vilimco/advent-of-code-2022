input_file = open('input.txt', 'r')
input = input_file.readlines()

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


sum = 0

for rawLine in input:
    line = rawLine.strip()
    if line == "":
        continue

    length = len(line)
    comp1 = list(line[slice(0, length//2)])
    comp2 = list(line[slice( length//2, length)])

    overlap = intersection(comp1, comp2)[0]
    match = ord(overlap)

    if match > 96:
        value = match - 96
    else:
        value = match - 65 + 27

    sum += value


print("Sum:", sum)
