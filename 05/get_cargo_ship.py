from collections import defaultdict
import re
from dataclasses import dataclass
from copy import deepcopy


@dataclass
class CargoDirection:
    move_: int
    from_: int
    to_: int


extract_direction = lambda x : CargoDirection(*map(int, re.findall('\d+', x)))
get_top_cargo = lambda x : "".join([x[i][-1] for i in range(1, max(x.keys()) + 1)])


def find_separator(raw_cargo_data: list[str]) -> int:
    for index, line in enumerate(raw_cargo_data):
        if line.replace(" ", "").isnumeric():
            return index


def convert_to_cargo_map_and_directions(
    raw_cargo_data: list[str]
) -> tuple[dict[int, list[str]], list[CargoDirection]]:
    separator = find_separator(raw_cargo_data)

    cargo_map = defaultdict(list)

    for cargo in raw_cargo_data[separator - 1::-1]:
        for index, item in enumerate(cargo[1::4], 1):
            if item != " ":
                cargo_map[index].append(item)

    return (cargo_map, list(map(extract_direction, raw_cargo_data[separator + 2:])))


def move_cargo(
    cargo_map: dict[int, list[str]],
    cargo_directions: list[CargoDirection],
    reverse: bool = False,
) -> dict[int, list[str]]:

    slice_direction = -1 if reverse else 1

    for direction in cargo_directions:
        cargo_map[direction.to_] += cargo_map[direction.from_][-direction.move_:][::slice_direction]
        cargo_map[direction.from_] = cargo_map[direction.from_][:-direction.move_]
    return cargo_map


if __name__ == "__main__":

    with open("05_input.txt", "r") as f:
            raw_cargo_data = f.read().splitlines()

    initial_cargo_map, cargo_directions = convert_to_cargo_map_and_directions(raw_cargo_data)

    reverse_order = move_cargo(deepcopy(initial_cargo_map), cargo_directions, reverse=True)
    normal_order = move_cargo(deepcopy(initial_cargo_map), cargo_directions)

    top_reverse_order = get_top_cargo(reverse_order)
    top_normal_order = get_top_cargo(normal_order)

    print(f"{top_reverse_order=}", f"{top_normal_order=}", sep="\n")
