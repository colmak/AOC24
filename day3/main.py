import os
import re

def read_file(fname):
    if not os.path.exists(fname):
        raise Exception(f"File {fname} not found!")

    with open(fname, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        return lines

def part1(lines):
    tol = 0
    res = []
    for line in lines:
        matches = re.findall(r'mul\((\d+),(\d+)\)', line)
        res.append([int(a) * int(b) for a, b in matches])
        
    for r in res:
        for i in r:
            tol+=i
    
    print(tol)


def part2(lines):
    tol = 0
    res = []
    enabled = True


    for line in lines:
        matches = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", line)
        
        for match in matches:
            if match == "don't()":
                enabled = False 
            elif match == "do()":
                enabled = True
            elif enabled and match.startswith("mul"):
                a, b = map(int, re.findall(r"\d+", match))
                res.append(a * b)

    for r in res:
        tol+=r

    print(tol)

    
    pass

def main():
    lines = read_file("day3/input.txt")
    # part1(lines)
    part2(lines)

if __name__ == "__main__":
    main()