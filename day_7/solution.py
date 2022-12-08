input_file = "day_7/input.data"
 
def handle_command(cmd, pos):
    if cmd == "cd ..":
        pos.pop()
    elif cmd == "cd /":
        pass
    elif cmd.startswith("cd"):
        dir = cmd[3:]
        pos.append(dir)
    elif cmd.startswith("ls"):
        pass
    else:
        print(f"Unknown command! ({cmd})")

def get_folder(path, dir):
    for key in path:
        dir = dir[key]
    return dir

def add_dir(dir, pos, fs):
    folder = get_folder(pos, fs)
    folder[dir] = {}
    
def add_file(size, file, pos, fs):
    folder = get_folder(pos, fs)
    folder[file] = int(size)

def get_folder_size(folder):
    sum = 0
    for key, value in folder.items():
        if isinstance(value, int):
            sum += value
        else:
            sum += get_folder_size(value)
    return sum

def get_all_folder_sizes(path, contents, sums):
    sums[path] = get_folder_size(contents)
    for key, value in contents.items():
        if type(value) is dict:
            get_all_folder_sizes(path + "/" + key, value, sums)
    return sums

with open(input_file, "r") as file:
    filesystem = {"/": {}}
    pos = ["/"]
    for l in file.readlines():
        if l.startswith("$"):
            cmd = l[2:].strip()
            handle_command(cmd, pos)
        elif l.startswith("dir"):
            add_dir(l[4:].strip(), pos, filesystem)
        elif l[0].isdigit():
            add_file(*l.split(), pos, filesystem)
    all_sizes = get_all_folder_sizes("/", filesystem["/"], {})
    available_space = 70000000 - all_sizes["/"]
    update_size = 30000000
    needed_size = update_size - available_space
    print(sum([x for x in all_sizes.values() if x <= 100000]))
    print(sorted([x for x in all_sizes.values() if x >= needed_size])[0])
