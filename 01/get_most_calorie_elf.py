

def get_top_x_elves_with_most_calories(
    top_num_of_elves: int,
    input_file_name: str = "01_input.txt"
) -> list[int]:

    with open(input_file_name, "r") as f:
        list_of_calories = f.read().splitlines()

    all_weights = []
    weight = 0

    while list_of_calories:
        next_cal = list_of_calories.pop()
        if next_cal:
            weight += int(next_cal)
        else:
            all_weights.append(weight)
            weight = 0

    return sorted(all_weights)[-top_num_of_elves:]

if __name__ == "__main__":

    top_1_elves_calories = sum(get_top_x_elves_with_most_calories(1))
    top_3_elves_calories = sum(get_top_x_elves_with_most_calories(3))

    print(f"{top_1_elves_calories=}", f"{top_3_elves_calories=}", sep="\n")
