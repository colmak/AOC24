import os
def read_file(fname):
    if not os.path.exists(fname):
        raise Exception(f"File {fname} not found!")

    with open(fname, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        return lines

def part1(lines):
    split_lines = [line.split("   ") for line in lines]
    
    first_elements = []
    for split_line in split_lines:
        if split_line:
            first_elements.append(split_line[0])

    second_elements = []
    for split_line in split_lines:
        if split_line:
            second_elements.append(split_line[1])
    
    first_elements.sort()
    second_elements.sort()
    
    
    tol = 0
    
    for i in range(len(first_elements)):
        tol += abs(int(first_elements[i]) - int(second_elements[i]))
        
    print(tol)


def part2(lines):
    split_lines = [line.split("   ") for line in lines]
    
    first_elements = []
    for split_line in split_lines:
        if split_line:
            first_elements.append(split_line[0])

    second_elements = []
    for split_line in split_lines:
        if split_line:
            second_elements.append(split_line[1])
    
    first_elements.sort()
    second_elements.sort()
    
    
    s_e_counts = {}
    for i in second_elements:
        if i in s_e_counts:
            s_e_counts[i] += 1
        else:
            s_e_counts[i] = 1
            
    tol = 0
        
    for i in range(len(first_elements)):
        if first_elements[i] not in s_e_counts:
            continue
        tol+=int(first_elements[i])*s_e_counts[first_elements[i]]
    print(tol)

def main():
    lines = read_file("day1/input.txt")
    # part1(lines)
    part2(lines)

if __name__ == "__main__":
    main()