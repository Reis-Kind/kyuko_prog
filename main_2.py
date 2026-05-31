def solve_maze(maze):
    rows = len(maze)
    cols = len(maze[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while True:
        updated = False

        for y in range(rows):
            for x in range(cols):
                if maze[y][x] == 0:
                    wall_count = 0

                    for dy, dx in directions:
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < rows and 0 <= nx < cols:
                            if maze[ny][nx] == 1:
                                wall_count += 1
                        else:
                            wall_count += 1

                    if wall_count >= 3:
                        maze[y][x] = 1
                        updated = True

        if not updated:
            break

    return maze


def print_maze(maze):
    for row in maze:
        row_str = ""
        for cell in row:
            if cell == 1:
                row_str += "■ "
            elif cell == 0:
                row_str += "□ "
            elif cell == 8:
                row_str += "Ｓ "
            elif cell == 9:
                row_str += "Ｇ "
        print(row_str)


initial_maze = [
    [1, 1, 1, 8, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 9, 1, 1, 1]
]

print("--- 初期状態 (図3) ---")
print_maze(initial_maze)

result_maze = solve_maze(initial_maze)

print("\n--- 全ての袋小路を埋めた結果 (図2) ---")
print_maze(result_maze)