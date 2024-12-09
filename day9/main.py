import os

def read_file(fname):
    if not os.path.exists(fname):
        raise Exception(f"File {fname} not found!")

    with open(fname, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        return lines

def parse_input(input_file_str):
    n = len(input_file_str)
    str_builder = []
    cur_index = 0
    for i in range(n):
        num = int(input_file_str[i])
        if i % 2 == 0:
            new_str_part = [str(cur_index)] * num
            str_builder.extend(new_str_part)
            cur_index += 1
        else:
            new_str_part = ["."] * num
            str_builder.extend(new_str_part)
    return str_builder

def part1(lines):
    str_builder = parse_input(lines[0])

    i_left, i_right = 0, len(str_builder) - 1
    while i_left < i_right:
        while str_builder[i_left] != ".":
            i_left += 1
        while str_builder[i_right] == ".":
            i_right -= 1
        right = str_builder[i_right]
        left = str_builder[i_left]
        if i_left < i_right:
            str_builder[i_left] = right
            str_builder[i_right] = left

    check_sum = 0
    for i, char in enumerate(str_builder):
        if char == ".":
            break
        check_sum += i * int(char)

    print(f"Checksum: {check_sum}")

def part2(lines):
    file_blocks, free_spaces, position = [], [], 0
    
    for index, char in enumerate(lines[0]):
        num = int(char)
        if index % 2 == 0:
            file_blocks.append(list(range(position, position + num)))
            position += num
        else:
            free_spaces.append(list(range(position, position + num)))
            position += num

    for file_block in reversed(file_blocks):
        for free_space in free_spaces:
            if len(free_space) >= len(file_block) and file_block[0] > free_space[0]:
                file_block[:] = free_space[:len(file_block)]
                del free_space[:len(file_block)]

    checksum = sum(i * j for i, block in enumerate(file_blocks) for j in block)
    print(f"Checksum Part 2: {checksum}")

def main():
    lines = read_file("day9/input.txt")
    part1(lines)
    part2(lines)

if __name__ == "__main__":
    main()
