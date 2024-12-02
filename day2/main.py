import os
def read_file(fname):
    if not os.path.exists(fname):
        raise Exception(f"File {fname} not found!")

    with open(fname, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        return lines

def part1(lines):
    # print(lines)
    
    reports = [l.split("\n") for l in lines]
    reports = [r[0].split(" ") for r in reports]

    def is_stepwise(sequence):
        sequence = [int(x) for x in sequence]
        differences = [sequence[i] - sequence[i - 1] for i in range(1, len(sequence))]
        
        return all(1 <= abs(diff) <= 3 for diff in differences) and (
            all(diff > 0 for diff in differences) or all(diff < 0 for diff in differences)
        )
    
    save_total = sum(1 for report in reports if is_stepwise(report))
            
    print(save_total)
    pass


def part2(lines):
    reports = [l.split("\n") for l in lines]
    reports = [r[0].split(" ") for r in reports]

    def is_safe(sequence):
        sequence = [int(x) for x in sequence] 
        differences = [sequence[i] - sequence[i - 1] for i in range(1, len(sequence))]

        return all(1 <= abs(diff) <= 3 for diff in differences) and (
            all(diff > 0 for diff in differences) or all(diff < 0 for diff in differences)
        )

    def can_be_safe(sequence):
        for i in range(len(sequence)):
            # Create a new sequence without the ith level
            new_sequence = sequence[:i] + sequence[i + 1:]
            if is_safe(new_sequence):
                return True
        return False
    
    save_total = 0
    for report in reports:
        if is_safe(report) or can_be_safe(report):
            save_total += 1
    
    print(save_total)
    pass

def main():
    lines = read_file("day2/input.txt")
    # part1(lines)
    part2(lines)

if __name__ == "__main__":
    main()