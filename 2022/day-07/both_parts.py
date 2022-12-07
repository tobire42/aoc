class File():
    def __init__(self, name, size, directory):
        self.name = name
        self.size = size
        self.directory = directory
        self.directory.add_item(self)

class Directory():
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.contents = []
        self.total_size = None
        if self.parent:
            self.parent.add_item(self)
    
    def add_item(self, item):
        self.contents.append(item)

    def get_child_dir(self, name):
        for d in self.contents:
            if isinstance(d, Directory) and d.name == name:
                return d

    def get_total_size(self):
        if self.total_size:
            return self.total_size
        total_size = 0
        for item in self.contents:
            if isinstance(item, Directory):
                total_size += item.get_total_size()
            elif isinstance(item, File):
                total_size += item.size
        self.total_size = total_size
        return total_size

    def get_path(self):
        path = [self.name]
        curdir = self
        while curdir.parent:
            curdir = curdir.parent
            path.append(curdir.name)
        return reversed(path)

    def get_all_subdirs(self):
        dirs = []
        dirs.append(self)
        for item in self.contents:
            if isinstance(item, Directory):
                dirs.append(item)
                dirs += item.get_all_subdirs()
        return dirs

    def add_sizes_below_threshold(self, threshold=100000):
        print(" / ".join(self.get_path()))
        
        total_size = 0
        if self.get_total_size() <= threshold:
            total_size += self.get_total_size()
        
        for item in self.contents:
            if isinstance(item, Directory):
                total_size += item.add_sizes_below_threshold()
        return total_size


    def __repr__(self):
        return f"Directory {self.name} Contents: {self.contents}"


def get_file_tree():
    top_dir = Directory("/", None)
    current_dir = top_dir
    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()
            splitted_line = line.split(" ")
            if splitted_line[0] == "$":
                if splitted_line[1] == "cd":
                    if splitted_line[2] == "..":
                        current_dir = current_dir.parent
                    elif splitted_line[2] == "/":
                        current_dir = top_dir
                    else:
                        current_dir = current_dir.get_child_dir(splitted_line[2])
            else:
                if splitted_line[0] == "dir":
                    Directory(splitted_line[1], current_dir)
                else:
                    File(splitted_line[1], int(splitted_line[0]), current_dir)
    return top_dir

def find_best_dir_to_delete(tree, total_disk_space=70000000, needed_unused_space=30000000):
    used_space = tree.get_total_size()
    unused_space = total_disk_space - used_space
    space_to_free_up = needed_unused_space - unused_space

    dirs = tree.get_all_subdirs()
    dir_sizes = sorted([dir.get_total_size() for dir in dirs])
    for size in dir_sizes:
        if size >= space_to_free_up:
            return size

if __name__ == "__main__":
    tree = get_file_tree()
    part1 = tree.add_sizes_below_threshold()
    part2 = find_best_dir_to_delete(tree)
    print(f"Part 1: {part1} Part 2: {part2}")

