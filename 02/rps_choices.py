from enum import Enum

LOSE_PTS, DRAW_PTS, WIN_PTS = (0, 3, 6)

class GamePoints(Enum):
    WIN: int = 6
    DRAW: int = 3
    LOSE: int = 0

class PlayerRPS(Enum):
    ROCK: int = 1
    PAPER: int = 2
    SCISSORS: int = 3


class RPS_Choice:
    def __init__(
        self,
        same: PlayerRPS,
        win: PlayerRPS,
        lose: PlayerRPS,
    ):
        self.same = same
        self.win = win
        self.lose = lose

    def __new__(cls, *args, **kwargs):
        # make it so this class is only instantiated once
        if not hasattr(cls, "instance"):
            cls.instance = super(RPS_Choice, cls).__new__(cls)
        return cls.instance

    def get_rps_type(self) -> PlayerRPS:
        return self.same

    def pick_score(self, determined_result: GamePoints) -> int:
        return self.same.value + determined_result.value

    def determine_score(self, player_move: PlayerRPS) -> int:
        score = self.same.value

        match player_move:
            case self.win:
                score += GamePoints.WIN.value
            case self.same:
                score += GamePoints.DRAW.value
            case self.lose:
                score += GamePoints.LOSE.value

        return score

    def determine_opponents_score(self, result: GamePoints) -> int:
        score = result.value

        match result:
            case GamePoints.WIN:
                score += self.lose.value
            case GamePoints.DRAW:
                score += self.same.value
            case GamePoints.LOSE:
                score += self.win.value

        return score

class Rock(RPS_Choice):
    def __init__(self):
        super().__init__(
            same=PlayerRPS.ROCK,
            win=PlayerRPS.SCISSORS,
            lose=PlayerRPS.PAPER,
        )


class Paper(RPS_Choice):
    def __init__(self):
        super().__init__(
            same=PlayerRPS.PAPER,
            win=PlayerRPS.ROCK,
            lose=PlayerRPS.SCISSORS,
        )

class Scissors(RPS_Choice):
    def __init__(self):
        super().__init__(
            same=PlayerRPS.SCISSORS,
            win=PlayerRPS.PAPER,
            lose=PlayerRPS.ROCK,
        )
