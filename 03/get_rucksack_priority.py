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
    iter_rucksacks = all_rucksacks[:]

    while iter_rucksacks:
        rucksacks_in_question, iter_rucksacks = iter_rucksacks[:n], iter_rucksacks[n:]
        shared_elements = set(rucksacks_in_question[0])
        for i in range(1, n):
            shared_elements = shared_elements.intersection(set(rucksacks_in_question[i]))

        running_priority += PRIORITY_MAP[shared_elements.pop()]

    return running_priority


if __name__ == "__main__":
    with open("03_input.txt", "r") as f:
        all_rucksacks = f.read().splitlines()

    pt1 = get_single_rucksack_shared_item_priority(all_rucksacks)
    pt2 = get_multiple_rucksack_shared_item_priority(all_rucksacks)

    print(f"{pt1=}", f"{pt2=}", sep="\n")
