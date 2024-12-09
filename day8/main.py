import os

def calc(a, b, dx, dy, antinodes, y):
    while True:
        if not (0 <= a < y + 1 and 0 <= b < y + 1):
            return
        antinodes.add((a, b))
        a, b = a + dx, b + dy

def read_file(fname):
    if not os.path.exists(fname):
        raise Exception(f"File {fname} not found!")

    with open(fname, 'r') as f:
        return [l.strip() for l in f.readlines()]

def part1(lines):
    frequencies = [[] for n in range(75)]
    antinodes = set()

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c != '.':
                frequencies[ord(c) - 48].append((x, y))

    for frequency in frequencies:
        for i, antenna1 in enumerate(frequency):
            for antenna2 in frequency[i + 1:]:
                antinodes |= {(antenna1[0] * 2 - antenna2[0], antenna1[1] * 2 - antenna2[1]), (antenna2[0] * 2 - antenna1[0], antenna2[1] * 2 - antenna1[1])}
                if (antenna1[0] - antenna2[0]) % 3 == 0 and (antenna1[1] - antenna2[1]) % 3 == 0:
                    dx, dy = (antenna1[0] - antenna2[0]) // 3, (antenna1[1] - antenna2[1]) // 3
                    antinodes |= {(antenna1[0] - dx, antenna1[1] - dy), (antenna1[0] - 2 * dx, antenna1[1] - 2 * dy)}

    print(sum([1 for antinode in antinodes if 0 <= antinode[0] < len(lines[0]) and 0 <= antinode[1] < len(lines)]))

def part2(lines):
    frequencies = [[] for n in range(75)]
    antinodes = set()

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c != '.':
                frequencies[ord(c) - 48].append((x, y))

    for frequency in frequencies:
        for i, antenna1 in enumerate(frequency):
            for antenna2 in frequency[i + 1:]:
                dx, dy = antenna1[0] - antenna2[0], antenna1[1] - antenna2[1]
                calc(antenna1[0], antenna1[1], dx, dy, antinodes, len(lines))
                calc(antenna1[0], antenna1[1], -dx, -dy, antinodes, len(lines))
                calc(antenna2[0], antenna2[1], dx, dy, antinodes, len(lines))
                calc(antenna2[0], antenna2[1], -dx, -dy, antinodes, len(lines))

    print(len(antinodes))

def main():
    lines = read_file("day8/input.txt")
    # part1(lines)
    part2(lines)

if __name__ == "__main__":
    main()