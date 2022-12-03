from rps_choices import (
    GamePoints,
    Rock,
    Paper,
    Scissors
)

RPS_CHOICE_MAP = {
    "A": Rock(),
    "B": Paper(),
    "C": Scissors(),
    "X": Rock(),
    "Y": Paper(),
    "Z": Scissors(),
}

PLAYER_DETERMINE_RESULT_MAP = {
    "X": GamePoints.LOSE,
    "Y": GamePoints.DRAW,
    "Z": GamePoints.WIN,
}

def read_02_input(file_name: str =  "02_input.txt") -> list[tuple[str, str]]:

    with open("02_input.txt", "r") as f:
        all_lines = f.read().splitlines()

    return list(map(lambda x: x.split(" "), all_lines))

def pt_1_scoring(actions: list[tuple[str, str]]) -> int:
    score = 0

    for opponent_signal, player_signal in actions:
        opponent_move = RPS_CHOICE_MAP[opponent_signal]
        player_move = RPS_CHOICE_MAP[player_signal]
        score += player_move.determine_score(opponent_move.get_rps_type())

    return score

def pt_2_scoring(actions: list[tuple[str, str]]) -> int:
    score = 0

    for opponent_signal, player_signal in actions:
        opponent_move = RPS_CHOICE_MAP[opponent_signal]
        expected_result = PLAYER_DETERMINE_RESULT_MAP[player_signal]

        score += opponent_move.determine_opponents_score(expected_result)

    return score

if __name__ == "__main__":
    actions = read_02_input()

    pt_1_score = pt_1_scoring(actions)
    pt_2_score = pt_2_scoring(actions)

    print(f"{pt_1_score=}", f"{pt_2_score=}", sep="\n")
