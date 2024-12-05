import os
import re

def read_file(fname):
    if not os.path.exists(fname):
        raise Exception(f"File {fname} not found!")

    with open(fname, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        return lines

def part1(lines):
    xmasCount = 0

    def rowCount(lines):
        xmasCount = 0
        for line in lines:
            xmasCount += len(re.findall(r'(?=(xmas|samx))', line, re.IGNORECASE))
        return xmasCount

    def getDiagonals(lines):
        diagonals = []

        # Top-left to bottom-right diagonals
        for offset in range(-len(lines) + 1, len(lines[0])):
            diagonal = [lines[i][i - offset] for i in range(len(lines)) if 0 <= i - offset < len(lines[0])]
            diagonals.append(''.join(diagonal))

        # Top-right to bottom-left diagonals
        for offset in range(-len(lines) + 1, len(lines[0])):
            diagonal = [lines[i][len(lines[0]) - 1 - i - offset] for i in range(len(lines)) if 0 <= len(lines[0]) - 1 - i - offset < len(lines[0])]
            diagonals.append(''.join(diagonal))

        return diagonals

    # Count horizontal matches
    xmasCount += rowCount(lines)

    # Count vertical matches (transpose the grid)
    transposed_lines = [''.join(row) for row in zip(*lines)]
    xmasCount += rowCount(transposed_lines)

    # Count diagonal matches
    diagonals = getDiagonals(lines)
    xmasCount += rowCount(diagonals)

    print(xmasCount)


def part2(lines):
    def count_xmas(grid):
        rows = len(grid)
        cols = len(grid[0])
        xmas_count = 0

        def is_valid_xmas(x, y):
            if (
                x - 1 >= 0 and y - 1 >= 0 and grid[x - 1][y - 1] in {'M', 'S'}
                and x + 1 < rows and y + 1 < cols and grid[x + 1][y + 1] in {'M', 'S'}
            ):
                diagonal_1 = grid[x - 1][y - 1] + grid[x][y] + grid[x + 1][y + 1]
                if diagonal_1 == "MAS" or diagonal_1 == "SAM":
                    if (
                        x - 1 >= 0 and y + 1 < cols and grid[x - 1][y + 1] in {'M', 'S'}
                        and x + 1 < rows and y - 1 >= 0 and grid[x + 1][y - 1] in {'M', 'S'}
                    ):
                        diagonal_2 = grid[x - 1][y + 1] + grid[x][y] + grid[x + 1][y - 1]
                        if diagonal_2 == "MAS" or diagonal_2 == "SAM":
                            return True
            return False

        for x in range(1, rows - 1): 
            for y in range(1, cols - 1):  
                if grid[x][y] == 'A':  
                    if is_valid_xmas(x, y):
                        xmas_count += 1
        return xmas_count
    print(count_xmas(lines))

def main():
    lines = read_file("day4/input.txt")
    # part1(lines)
    part2(lines)

if __name__ == "__main__":
    main()