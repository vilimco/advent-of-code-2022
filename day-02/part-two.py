input_file = open('input.txt', 'r')
input = input_file.readlines()

def get_round_score(opponent, me):
    # lose
    if me == 0:
        return (opponent - 1) % 3 + 1

    # draw
    if me == 1:
        return opponent + 1 + 3

    # win
    return (opponent + 1) % 3 + 1 + 6


score = 0
for rawLine in input:
    if rawLine.strip() == "":
        continue

    opponent, me = rawLine.strip().split(sep=" ")

    opponent = ord(opponent) - ord('A')
    me = ord(me) - ord('X')

    score += get_round_score(opponent, me)

print("Final score:", score)
