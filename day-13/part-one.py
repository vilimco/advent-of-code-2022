import json

input_file = open('input.txt', 'r')
input = [value.strip() for value in input_file.readlines()]


def compare_elements(el1, el2):
    # If both are integers, compare
    if isinstance(el1, int) and isinstance(el2, int):
        if el2 < el1:
            raise TypeError("invalid order")
        elif el1 < el2:
            raise BufferError("valid order")
        return

    # if both lists, normal compare
    if not isinstance(el1, int) and not isinstance(el2, int):
        for el_idx in range(0, len(el1)):
            if el_idx >= len(el2):
                raise TypeError("invalid order, no second array")
            compare_elements(el1[el_idx], el2[el_idx])

        if len(el1) < len(el2):
            raise BufferError("valid order")
        return

    # one is list, other is integer
    if isinstance(el1, int):
        compare_elements([el1], el2)
    else:
        compare_elements(el1, [el2])


sum = 0

for i in range(0, len(input), 3):
    code1 = json.loads(input[i])
    code2 = json.loads(input[i + 1])

    try:
        compare_elements(code1, code2)
    except TypeError:
        print("Not in order")
    except BufferError:
        sum += int(i / 3 + 1)
        print("In order")

print("Sum", sum)
