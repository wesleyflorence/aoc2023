import aoc
import re

def words_to_digits(text):
    pattern = r'(one|two|three|four|five|six|seven|eight|nine)'
    word_to_digit = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4', 
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }
    return re.sub(pattern, lambda m: word_to_digit[m.group(0)], text)

def make_explicit(text):
    pattern = r'zerone|oneight|twone|sevenine|eightwo|eighthree|nineight'
    subs = {
        "zerone": "zeroone",
        "oneight": "oneeight",
        "twone": "twoone",
        "sevenine": "sevennine",
        "eightwo": "eighttwo",
        "eighthree": "eightthree",
        "nineight": "nineeight"
    }
    return re.sub(pattern, lambda m: subs[m.group(0)], text)

def calc(input):
    total = 0
    for line in input:
        num_str = ''.join([c for c in line if c.isdigit()])
        total += int(num_str[0] + num_str[-1])
    return total

def part_one(input):
    return calc(input)

def part_two(input):
    return calc(words_to_digits(make_explicit(l)) for l in input)

input = aoc.read_input("01")
p1 = part_one(input)
p2 = part_two(input)
print(f"Part One: {p1}")
print(f"Part Two: {p2}")

