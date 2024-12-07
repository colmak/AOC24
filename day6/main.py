import os

def read_file(fname):
    if not os.path.exists(fname):
        raise Exception(f"File {fname} not found!")

    with open(fname, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        return lines

def parse_input(lines):
    rows = lines
    width, height = len(rows[0]), len(rows)
    sx, sy = next((x, y) for y, row in enumerate(rows) for x, c in enumerate(row) if c in "<>v^")
    
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    direction_map = {
        ">": (1, 0),
        "<": (-1, 0),
        "^": (0, -1),
        "v": (0, 1)
    }
    
    return rows, width, height, sx, sy, directions, direction_map

def get_jump_location(rows, width, height, x, y, dindex, directions):
    if rows[y][x] == "#":
        return None

    dx, dy = directions[dindex]
    while x >= 0 and y >= 0 and x < width and y < height and rows[y][x] != "#":
        x += dx
        y += dy

    if x < 0 or y < 0 or x >= width or y >= height:
        return (x, y, None)

    x -= dx
    y -= dy
    dindex = (dindex + 1) % 4
    return (x, y, dindex)

def build_jump_map(rows, width, height, directions):
    return {
        (x, y, di): get_jump_location(rows, width, height, x, y, di, directions)
        for x in range(width) for y in range(height) for di in range(len(directions))
    }

def jump_into_block(dindex, block_patch, directions):
    dx, dy = directions[dindex]
    bx, by = block_patch
    return (bx - dx, by - dy, (dindex + 1) % 4)

def jump(jump_map, x, y, dindex, block_patch, directions):
    dest = jump_map.get((x, y, dindex))
    if block_patch is not None and dest is not None:
        fx, fy, _ = dest
        bx, by = block_patch
        if fx == bx and min(y, fy) <= by <= max(y, fy):
            return jump_into_block(dindex, block_patch, directions)
        elif min(x, fx) <= bx <= max(x, fx) and fy == by:
            return jump_into_block(dindex, block_patch, directions)
    return dest

def get_full_path(rows, width, height, sx, sy, directions, direction_map):
    x, y = sx, sy
    visited = set()
    dindex = directions.index(direction_map[rows[y][x]])

    while True:
        visited.add((x, y))
        dx, dy = directions[dindex]
        x, y = x + dx, y + dy
        if x < 0 or y < 0 or x >= width or y >= height:
            break
        elif rows[y][x] == "#":
            x, y = x - dx, y - dy
            dindex = (dindex + 1) % len(directions)

    return visited

def path_loops_with_patch(rows, width, height, sx, sy, directions, direction_map, jump_map, block_patch):
    x, y = sx, sy
    dindex = directions.index(direction_map[rows[y][x]])
    visited = set()

    while True:
        jump_result = jump(jump_map, x, y, dindex, block_patch, directions)
        if jump_result is None:
            return False

        x, y, dindex = jump_result

        if (x, y, dindex) in visited:
            return True

        visited.add((x, y, dindex))

def part1(lines):
    rows, width, height, sx, sy, directions, direction_map = parse_input(lines)
    path = get_full_path(rows, width, height, sx, sy, directions, direction_map)
    print(len(path))

def part2(lines):
    rows, width, height, sx, sy, directions, direction_map = parse_input(lines)
    jump_map = build_jump_map(rows, width, height, directions)

    path = get_full_path(rows, width, height, sx, sy, directions, direction_map)
    loop_positions = 0

    for block in path:
        if block != (sx, sy) and path_loops_with_patch(rows, width, height, sx, sy, directions, direction_map, jump_map, block):
            loop_positions += 1

    print(loop_positions)

def main():
    lines = read_file("day6/input.txt")
    # part1(lines)
    part2(lines)

if __name__ == "__main__":
    main()
