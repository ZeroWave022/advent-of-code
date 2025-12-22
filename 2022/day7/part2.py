import os
import re
from typing import Any

path = os.path.join(os.path.dirname(__file__), "day_7_input.txt")

with open(path, encoding="utf-8") as f:
    raw_data = f.read().splitlines()

def read_files_in_dir(all_lines: dict[str, Any], from_index: int):
    """Takes the whole input, and starting from 'from_index' reads files in the directory (ignores dirs).
    all_lines: dict[str, Any]
        The whole puzzle input
    from_index: int
        The index in all_lines where a ls command happened.
    
    Returns a list of files in the directory currently being listed.
    The files are a dict each with the file name (key) and size (value).
    """
    files: list[dict[str, str]] = []

    for dir_line in all_lines[from_index+1:]:
        if not dir_line.startswith("$") and not dir_line.startswith("dir"):
            filename = re.sub(r"\d| ", "", dir_line) # Remove size and space
            filesize = re.split(" ", dir_line, 1)[0] # Get whatever before the first space (the size)
            files.append({ filename: filesize })
        elif dir_line.startswith("$"):
            break

    return files

def directory_size(all_dirs: dict[str, Any], name: str):
    """Takes the whole input, and the name of the directory which shall get its size calculated."""
    # Filter out any sub-directories which are in this dir. Will also include itself.
    if name != "/":
        dirs_included = list(filter(lambda path: path.startswith(name), all_dirs))
    else:
        dirs_included = all_dirs
    dir_size = 0

    # Sum sizes of itself and any sub-directories
    for directory in dirs_included:
        dir_contents = dirs[directory]
        if len(dir_contents) < 1:
            continue
        for file in dir_contents:
            dir_size += int(list(file.values())[0]) # Only one value per file, and that is the file size

    return dir_size

dirs: dict[str, Any] = {}

current_dir: list[str] = []
for index, line in enumerate(raw_data):
    if line.startswith("$ cd"):
        next_dir = line.replace("$ cd ", "")
        if next_dir == "..":
            current_dir.pop()
        else:
            current_dir.append(next_dir)
    elif line.startswith("$ ls"):
        dir_name = "/".join(current_dir[1:]) if len(current_dir) > 1 else "/"
        dir_files = read_files_in_dir(raw_data, index)
        dirs[dir_name] = dir_files

space_left = 70_000_000 - directory_size(dirs, "/")
space_required = 30_000_000 - space_left

possible_dir_sizes = []

# Skip the root directory
dir_names = list(dirs.keys())[1:]

for name in dir_names:
    dir_size = directory_size(dir_names, name)
    if dir_size >= space_required:
        possible_dir_sizes.append(dir_size)

print(f"The size of the smallest dir, which if deleted will free enough space to start the update, is {min(possible_dir_sizes)}")
