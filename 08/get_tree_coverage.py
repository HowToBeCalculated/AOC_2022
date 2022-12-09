import numpy as np

tree_coverage = []
with open("08_input.txt", "r") as f:

    row_of_trees = []

    while (tree := f.read(1)):
        if tree == "\n":
            tree_coverage.append(row_of_trees)
            row_of_trees = []
        else:
            row_of_trees.append(int(tree))

tree_coverage = np.array(tree_coverage)
print(tree_coverage)

def get_visible_trees(
    row: list[int],
    reverse: bool = False,
) -> set[int]:

    visibility_line = -1
    visible_indexes = []

    iterator = list(enumerate(row))

    if reverse:
        iterator = tuple(reversed(iterator))

    for index, tree in iterator:
        if tree > visibility_line:
            visible_indexes.append(index)
            visibility_line = tree

    return set(visible_indexes)

def get_visible_trees_of_row(x: int, y: int, transposed: bool = False) -> set[tuple[int]]:
    forward_pass = get_visible_trees(y)
    reverse_pass = get_visible_trees(y, reverse=True)
    combined_pass = forward_pass.union(reverse_pass)

    if transposed:
        return set(map(lambda tree: (x, tree), combined_pass))
    else:
        return set(map(lambda tree: (tree, x), combined_pass))

def get_visible_trees_of_forest(forest):

    visible_trees = set()

    for x, y in enumerate(forest):
        visible_trees = visible_trees.union(get_visible_trees_of_row(x, y))

    for x, y in enumerate(forest.T):
        visible_trees = visible_trees.union(get_visible_trees_of_row(x, y, transposed=True))

    return len(visible_trees)

print(get_visible_trees_of_forest(tree_coverage))

def combine_dicts(dict1: dict, dict2: dict) -> dict:

    new_dict = {}

    for key in set(dict1.keys()).union(set(dict2.keys())):
        dict1_val = dict1.get(key, 1)
        dict2_val = dict2.get(key, 1)
        new_dict[key] = dict1_val * dict2_val

    return new_dict

def get_scenic_value_of_trees(
    row: list[int],
    reverse: bool = False,
) -> dict[int, int]:

    scenic_map = {}

    iterator = list(enumerate(row))

    if reverse:
        iterator = tuple(reversed(iterator))

    indexes = [index for index, _ in iterator]

    count = 0

    for index, tree in iterator:
        print(f"{index=}, {tree=}")
        scenic_map[index] = 0
        for prior_tree in indexes[:count][::-1]:
            print(f"{tree=} {prior_tree=}, {row[prior_tree]=}")
            scenic_map[index] += 1
            if tree <= row[prior_tree]:
                break
        count += 1
        print(scenic_map)
        print("~"*20)

    return scenic_map

def get_scenic_value_of_row_of_trees(x: int, y: int, transposed: bool = False) -> set[tuple[int]]:
    forward_pass = get_scenic_value_of_trees(y)
    reverse_pass = get_scenic_value_of_trees(y, reverse=True)
    combined_pass = combine_dicts(forward_pass, reverse_pass)

    if transposed:
        return {(x, tree): combined_pass[tree] for tree in combined_pass.keys()}
    else:
        return {(tree, x): combined_pass[tree] for tree in combined_pass.keys()}

def get_scenic_values_of_forest(forest):

    scenic_value_map = {}

    for x, y in enumerate(forest):
        scenic_value_map = combine_dicts(get_scenic_value_of_row_of_trees(x, y), scenic_value_map)
        print(scenic_value_map.get((4, 3)))

    for x, y in enumerate(forest.T):
        scenic_value_map = combine_dicts(get_scenic_value_of_row_of_trees(x, y, transposed=True), scenic_value_map)
        print(scenic_value_map.get((4, 3)))

    return scenic_value_map

print(max(get_scenic_values_of_forest(tree_coverage).values()))