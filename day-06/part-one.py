input_file = open('input.txt', 'r')
input = input_file.readlines()

codeline = input[0].strip()

message_length = 4
for i in range(0, len(codeline) - message_length + 1):
    code = codeline[i:i+message_length]
    code_set = set(code)

    if len(code_set) == message_length:
        print(i + message_length)
        break
