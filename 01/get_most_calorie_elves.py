

def get_top_x_elves_with_most_calories(
    top_num_of_elves: int,
    list_of_calories: list[str],
) -> list[int]:

    all_weights = []
    weight = 0

    while list_of_calories:
        next_cal = list_of_calories.pop()
        print(next_cal)
        if next_cal:
            weight += int(next_cal)
        else:
            all_weights.append(weight)
            weight = 0

    return sorted(all_weights, reverse=True)[:top_num_of_elves]

if __name__ == "__main__":

    with open("01_input.txt", "r") as f:
        list_of_calories = f.read().splitlines()

    top_1_elves_calories = sum(get_top_x_elves_with_most_calories(1, list_of_calories[:]))
    top_3_elves_calories = sum(get_top_x_elves_with_most_calories(3, list_of_calories[:]))

    print(f"{top_1_elves_calories=}", f"{top_3_elves_calories=}", sep="\n")
