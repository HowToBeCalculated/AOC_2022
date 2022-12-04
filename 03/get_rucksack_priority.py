import string

PRIORITY_MAP = {val: letter for letter, val in enumerate(string.ascii_letters, 1)}


def get_single_rucksack_shared_item_priority(all_rucksacks: list[str]) -> int:

    running_priority = 0

    for rucksack in all_rucksacks:
        half_len = int(len(rucksack) / 2)
        shared_element = set(rucksack[:half_len]).intersection(set(rucksack[half_len:])).pop()
        running_priority += PRIORITY_MAP[shared_element]

    return running_priority


def get_multiple_rucksack_shared_item_priority(all_rucksacks: list[str], n: int = 3) -> int:
    running_priority = 0
    iter_rucksacks = map(lambda x: set(x), all_rucksacks)

    while (rucksack := next(iter_rucksacks, None)):
        shared_elements = rucksack.intersection(*(next(iter_rucksacks, set()) for _ in range(n - 1)))
        running_priority += PRIORITY_MAP[shared_elements.pop()]

    return running_priority


if __name__ == "__main__":
    with open("03_input.txt", "r") as f:
        all_rucksacks = f.read().splitlines()

    pt1 = get_single_rucksack_shared_item_priority(all_rucksacks)
    pt2 = get_multiple_rucksack_shared_item_priority(all_rucksacks)

    print(f"{pt1=}", f"{pt2=}", sep="\n")
