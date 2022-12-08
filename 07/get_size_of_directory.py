from utils_07 import Node


def calculate_full_terminal_log_Node(terminal_logs: list[str]) -> Node:
    root = Node("root")
    cwd = root

    for log in (terminal_logs):
        log_item_name = log.split()[-1]

        if log.startswith("$ cd"):

            if log_item_name == "/":
                cwd = root
            elif log_item_name == "..":
                cwd = cwd.prior
            else:
                cwd = cwd.move_to_descendant(log_item_name)

        elif log.startswith("$ ls"):
            continue

        elif log.startswith("dir"):
            cwd.add_descendant(log_item_name)

        else:
            cwd.add_descendant(log_item_name, int(log.split()[0]))

    root.calculate_sizes()
    return root


def calculate_space_dedicated_to_directories_under_x_space(
    root: Node,
    max_space_per_directory: int = 100_000,
) -> int:

    current = root
    stack = [i for i in root.descendants.values()]
    applicable_dirs = []

    while stack:
        current = stack.pop()

        if current.descendants:
            stack.extend(current.descendants.values())
        else:
            # skips if not dir (as no descendants)
            continue

        if current.value <= max_space_per_directory:
            applicable_dirs.append(current)

    return sum(applicable_dirs)


def calculate_smallest_directory_space_to_delete(
    root: Node,
    needed_disk_space: int = 30_000_000,
    total_disk_space: int = 70_000_000,
) -> int:

    unused_space = total_disk_space - root.value
    space_to_free_up = needed_disk_space - unused_space

    current = root
    stack = [i for i in root.descendants.values()]
    smallest_directory_space_to_delete = float("inf")

    while stack:
        current = stack.pop()

        if current.descendants:
            stack.extend(current.descendants.values())
        else:
            # skips if not dir (as no descendants)
            continue

        if space_to_free_up <= current.value < smallest_directory_space_to_delete:
            smallest_directory_space_to_delete = current.value

    return smallest_directory_space_to_delete


if __name__ == "__main__":

    with open("07_input.txt", "r") as f:
        terminal_logs = f.read().splitlines()

    root = calculate_full_terminal_log_Node(terminal_logs)

    applicable_dir_space = calculate_space_dedicated_to_directories_under_x_space(root)
    smallest_directory_space_to_delete = calculate_smallest_directory_space_to_delete(root)

    print(f"Applicable directory space: {applicable_dir_space:,}")
    print(f"Smallest directory space to delete: {smallest_directory_space_to_delete:,}")