import json
import functools

input_file = open('input.txt', 'r')
input = [value.strip() for value in input_file.readlines()]
input = list(filter(lambda x: (x != ""), input))
input.append("[[2]]")
input.append("[[6]]")
input = [json.loads(value) for value in input]


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

def compare_pack(code1, code2):
    try:
        compare_elements(code1, code2)
    except TypeError:
        return 1
    except BufferError:
        return -1
    return 0


input = sorted(input, key=functools.cmp_to_key(compare_pack))

p1 = 0
p2 = 0

for idx, code in enumerate(input):
    raw_code = json.dumps(code)

    if raw_code == "[[2]]":
        p1 = idx + 1
    if raw_code == "[[6]]":
        p2 = idx + 1

print(p1 * p2)

