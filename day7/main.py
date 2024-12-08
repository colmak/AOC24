import os
from itertools import product

def read_file(fname):
    if not os.path.exists(fname):
        raise Exception(f"File {fname} not found!")

    with open(fname, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        return lines

def parse_input(lines):
    equations = {}
    for line in lines:
        test_value, numbers = line.split(":")
        test_value = int(test_value.strip())
        numbers = list(map(int, numbers.strip().split()))
        equations[test_value] = numbers
    return equations

def evaluate_expression(values, operators):
    result = values[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += values[i + 1]
        elif op == '*':
            result *= values[i + 1]
    return result

def evaluate_expression_with_concat(values, operators):
    result = values[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += values[i + 1]
        elif op == '*':
            result *= values[i + 1]
        elif op == '||':
            result = int(str(result) + str(values[i + 1]))
    return result

def evaluate_with_early_exit(numbers, target, current=0, index=0):
    if index == len(numbers):  
        return current == target

    if index == 0:  
        return evaluate_with_early_exit(numbers, target, numbers[0], index + 1)

    if evaluate_with_early_exit(numbers, target, current + numbers[index], index + 1):
        return True

    if evaluate_with_early_exit(numbers, target, current * numbers[index], index + 1):
        return True

    concatenated = int(str(current) + str(numbers[index]))
    if evaluate_with_early_exit(numbers, target, concatenated, index + 1):
        return True

    return False

def part1(lines):
    equations = parse_input(lines)
    total_calibration_result = 0
    valid_equations = []

    for test_value, numbers in equations.items():
        num_positions = len(numbers) - 1
        operator_combinations = product("+-*", repeat=num_positions)

        for operators in operator_combinations:
            if evaluate_expression(numbers, operators) == test_value:
                valid_equations.append(test_value)
                total_calibration_result += test_value
                break
    print(total_calibration_result)

def part2(lines):
    equations = parse_input(lines)
    total_calibration_result = 0
    valid_equations = []

    for test_value, numbers in equations.items():
        if evaluate_with_early_exit(numbers, test_value):
            valid_equations.append(test_value)
            total_calibration_result += test_value

    print(total_calibration_result)

def main():
    lines = read_file("day8/input.txt")
    part2(lines)

if __name__ == "__main__":
    main()


def main():
    lines = read_file("day8/input.txt")
    part2(lines)

if __name__ == "__main__":
    main()
