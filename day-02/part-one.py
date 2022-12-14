input_file = open('input.txt', 'r')
input = input_file.readlines()

def get_round_score(opponent, me):
    if opponent == me:
        return 3

    if (me - opponent) % 3 == 1:
        return 6

    return 0


score = 0
for rawLine in input:
    if rawLine.strip() == "":
        continue

    opponent, me = rawLine.strip().split(sep=" ")

    opponent = ord(opponent) - ord('A')
    me = ord(me) - ord('X')

    round_score = get_round_score(opponent, me) + me + 1
    score += round_score

print("Final score:", score)
