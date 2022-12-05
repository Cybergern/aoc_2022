input_file = "day_2/input.data"

first_part_scores = {"A X": 4, "A Y": 8, "A Z": 3, "B X": 1, "B Y": 5, "B Z": 9, "C X": 7, "C Y": 2, "C Z": 6}
second_part_scores = {"A X": 3, "A Y": 4, "A Z": 8, "B X": 1, "B Y": 5, "B Z": 9, "C X": 2, "C Y": 6, "C Z": 7}

with open(input_file, "r") as file:
    first_part_score = 0
    second_part_score = 0
    for l in file.readlines():
        first_part_score += first_part_scores.get(l.strip())
        second_part_score += second_part_scores.get(l.strip())
    
print(first_part_score)
print(second_part_score)