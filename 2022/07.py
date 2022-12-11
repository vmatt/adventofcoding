from copy import deepcopy

file = open("input.txt", 'r').read()
cmds = file.split("\n")
cmds.remove("")

current_path = []
directory_sizes = {}
reading_output = False
for i,cmd in enumerate(cmds):
    if reading_output:
        output = cmd.split(' ')
        if output[0] == 'dir':
            pass
        if output[0].isnumeric():
            file_size = int(output[0])
            file_name = output[1]
            full_file_path = deepcopy(current_path)
            # full_file_path.append(file_name)
            for i in range(1,len(current_path)+1):
                joined_path = "/".join(current_path[0:i])
                try:
                    directory_sizes[joined_path] += file_size
                except KeyError:
                    directory_sizes[joined_path] = file_size
    if cmd.startswith("$ "):
        reading_output = False
        output = cmd.split(" ")
        if len(output)==3:
            command = output[1]
            object = output[2]
            if command == 'cd':
                if object == "/":
                    current_path = ['.']
                elif object == '..':
                    current_path.pop(-1)
                else:
                    current_path.append(object)

        elif output[1] == 'ls':
            reading_output=True

under_100_000 = 0
# total_usage = sum(directory_sizes.values())
for size in directory_sizes.values():
    if size <= 100_000:
        under_100_000+=size

print(under_100_000)

currently_used = directory_sizes['.']
free_space = 70000000-currently_used
required_space = 30000000-free_space
sorted_folder_sizes = sorted(directory_sizes.values())
for s in sorted_folder_sizes:
    if s >= required_space:
        print(s)
        break




