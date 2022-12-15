input_file = open('input.txt', 'r')
input = [value.strip() for value in input_file.readlines()]


class File:
    def __init__(self, type, name, size):
        self.type = type
        self.name = name
        self.size = size
        self.children = {}
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent

    def add_child(self, child):
        self.children[child.name] = child
        child.set_parent(parent=self)

    def is_directory(self):
        return self.type == "dir"

    def get_child(self, name):
        return self.children[name]

    def get_parent(self):
        return self.parent

    def get_size(self):
        if not self.is_directory():
            return self.size

        sum = 0
        for childName in self.children:
            child = self.children[childName]
            sum += child.get_size()

        return sum


root = File("dir", "/", 0)
current_dir = root

idx = 0
while (idx < len(input)):
    line = input[idx].split(" ")

    if line == "":
        break

    if line[0] == "$":
        cmd = line[1]
        if cmd == "cd":
            dir_name = line[2]
            if dir_name == "/":
                current_dir = root
            elif dir_name == "..":
                current_dir = current_dir.get_parent()
            else:
                current_dir = current_dir.get_child(name=dir_name)

            # move to next command
            idx += 1
            continue
        elif cmd == "ls":
            # do nothing, just leave parser
            idx += 1
            continue

    # it's line parsing
    if line[0] == "dir":
        new_file = File(type="dir", name=line[1], size=0)
    else:
        new_file = File(type="file", name=line[1], size=int(line[0]))

    current_dir.add_child(child=new_file)
    idx += 1


def print_output(file, prefix):
    print(prefix, file.type, file.name, file.get_size())
    for childName in file.children:
        print_output(file.children[childName], prefix + "  ")


def get_big_dirs(file):
    sum = 0
    if file.is_directory():
        dir_size = file.get_size()
        if dir_size < 100000:
            sum += dir_size
    for childName in file.children:
        sum += get_big_dirs(file.children[childName])

    return sum

total_size = get_big_dirs(root)
print("Total size", total_size)
