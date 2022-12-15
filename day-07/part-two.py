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

        if self.size > 0:
            return self.size

        sum = 0
        for childName in self.children:
            child = self.children[childName]
            sum += child.get_size()

        self.size = sum

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

directories = list([])


def build_dir_list(file):
    if file.is_directory():
        directories.append(file)

    for childName in file.children:
        build_dir_list(file.children[childName])


build_dir_list(root)
directories = sorted(directories, key=lambda x: x.get_size())

unused_space = 70000000 - root.get_size()
min_size = 30000000 - unused_space
print("Unused size:", unused_space)
print("Min size:", min_size)

for dir in directories:
    if dir.get_size() >= min_size:
        print(dir.name, dir.get_size())
        break

