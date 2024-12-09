import os
def read_file(fname):
    if not os.path.exists(fname):
        raise Exception(f"File {fname} not found!")

    with open(fname, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        return lines

def part1(lines):
    print(lines)
    pass


def part2(lines):
    pass

def main():
    lines = read_file("day9/input.txt")
    part1(lines)
    # part2(lines)

if __name__ == "__main__":
    main()