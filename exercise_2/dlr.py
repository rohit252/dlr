# -*- coding: utf-8 -*-


####### part 1
from enum import Enum

#define enumerate type to keep the check on the numbers of the cubes
class Color(Enum):
    RED = "red"
    BLUE = "blue"
    GREEN = "green"


file_path = "input1.txt"
##### read input from here
def read_input_file():
    with open(file_path) as f:
        lines = f.read().splitlines()
    return lines

#### if the number of cubes is less than the specified number than add the id of the games here
def sum_ids(lines):
    solution = 0

    for line in lines:
        game_id, combinations = line_splitting(line)
        if combinations_are_possible(combinations):
            solution += game_id

    return solution

##### splitting the id and all the possible combinations
def line_splitting(line):
    game, all_combinations = line.split(": ")
    game_id = int(game.replace("Game ", ""))
    # print(game_id)
    combinations = all_combinations.split("; ")
    samples = [sample_combination(combination) for combination in combinations]

    return game_id, samples

    
####### this function will create the dictionary to store the counter of combinations for every game
def sample_combination(sample_str):
    # "3 blue, 4 red"
    color_strings = sample_str.split(", ")
    color_dict = {}
    for color_str in color_strings:
        amount_str, color_str = color_str.split(" ")
        color_dict[color_str] = int(amount_str)
        
        # print(color_dict)

    return {
        color: color_dict.get(color.value, 0)
        for color in Color
    }

###### this function will check if the bag contains cubes less than 12 red, 13 and 14 blue cubes for every game 
def combinations_are_possible(combinations):
    for combination in combinations:
        if combination[Color.RED] > 12 or combination[Color.GREEN] > 13 or combination[Color.BLUE] > 14:
            return False
    return True

#### calling the function here                
solution_part1= sum_ids(read_input_file())
print('part 1 solution: ', solution_part1)



# def line_splitting(line):
#     game, all_combinations = line.split(": ")
#     game_id = int(game.replace("Game ", ""))
#     combinations = all_combinations.split("; ")
#     samples = []
#     for combination in combinations:
#         color_dict = {}
#         color_strings = combination.split(", ")
#         for color_str in color_strings:
#             amount_str, color_str = color_str.split(" ")
#             color_dict[color_str] = int(amount_str)
#         sample = {
#             color: color_dict.get(color.value, 0)
#             for color in Color
#         }
#         samples.append(sample)
#     return game_id, samples




###### part 2 ##########


def power(lines):
    solution = 0
    for line in lines:
        game_id, combinations = line_splitting(line)
        max_seen = dict.fromkeys(Color, 0)
        for combination in combinations:
            for color in Color:
                max_seen[color] = max(max_seen[color], combination[color])

        game_power = max_seen[Color.RED] * max_seen[Color.GREEN] * max_seen[Color.BLUE]
        solution += game_power
    return solution

#### calling the function here                
solution_part2 = power(read_input_file())
print('part 2 solution: ', solution_part2)