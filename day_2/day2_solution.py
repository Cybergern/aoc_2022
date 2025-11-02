input_file = "day_2/input.data"

FIRST_PART_SCORES = {"A X": 4, "A Y": 8, "A Z": 3, "B X": 1, "B Y": 5, "B Z": 9, "C X": 7, "C Y": 2, "C Z": 6}
SECOND_PART_SCORES = {"A X": 3, "A Y": 4, "A Z": 8, "B X": 1, "B Y": 5, "B Z": 9, "C X": 2, "C Y": 6, "C Z": 7}

def get_strategy_total(input_file: str, score_map: dict) -> int:
    score = 0
    with open(input_file, "r") as file:
        for l in file.readlines():
            score += score_map.get(l.strip())
    return score

def get_first_strategy_total(input_file: str) -> int:
    return get_strategy_total(input_file, FIRST_PART_SCORES)

def get_second_strategy_total(input_file: str) -> int:
    return get_strategy_total(input_file, SECOND_PART_SCORES)    
