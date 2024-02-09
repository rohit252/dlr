# -*- coding: utf-8 -*-



#### part1 ############

def sum(line):
    # Filter out non-numeric characters and take the first and last digits
    digits = [int(char) for char in line if char.isdigit()]
    if not digits:
        return 0  # Return 0 if no digits found
    first_digit = digits[0]
    last_digit = digits[-1]
    calibration_sum = first_digit * 10 + last_digit
    return calibration_sum

def calculate_sum(file_path):
    total_sum = 0
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            # Calculate value for the line
            calibration_value= sum(line)
            # Add value to the total sum
            total_sum += calibration_value
    return total_sum





file_path = 'input1.txt'
calibration_sum = calculate_sum(file_path)
print("Sum of all calibration values part1:", calibration_sum)


##### part2 #########

letters = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}


def first_digit(string):
    for index, character in enumerate(string):
        if character.isdigit(): 
            return int(character)

        remaining_string = string[index:]
        for digit, letter in letters.items():
            if remaining_string.startswith(letter):
                return digit
    # If no digit is found, return a default value (0)
    return 0


def last_digit(string):
    for end_position, character in enumerate(reversed(string)):
        if character.isdigit():
            return int(character)

        remaining_string = string[:len(string)-end_position]
        for digit, letter in letters.items():
            if remaining_string.endswith(letter):
                return digit
    # If no digit is found, return a default value (0)
    return 0


def sum():
    total_sum = 0
    with open(file_path_2) as f:
        for line in f:
            line = line.strip()
            # Calculate calibration value for the current line
            calibration_value = 10 * first_digit(line) + last_digit(line)
            total_sum += calibration_value
            # Add calibration value to the total sum
    return total_sum

   


file_path_2 = "input2.txt"
total_sum = sum()
print("Sum of all calibration values part2:", total_sum)

