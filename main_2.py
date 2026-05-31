def solve_maze(maze):
    """
    迷路の全ての袋小路を壁で埋めて解を返す。

    袋小路（上下左右4マスのうち3マス以上が壁のマス）を壁(1)に書き換える操作を、
    変化がなくなるまで繰り返す。最終的にスタートからゴールへの経路のみが残る。

    Args:
        maze (list[list[int]]): 2次元配列の迷路。
            0=道, 1=壁, 8=スタート, 9=ゴール。
            インデックスは maze[y][x]（0ベース）。

    Returns:
        list[list[int]]): 袋小路を全て壁(1)で埋めた後の迷路。
            引数の maze を直接書き換えて返す。
    """
    rows = len(maze)
    cols = len(maze[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    updated = True

    while updated:
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

    return maze


def print_maze(maze):
    """
    迷路を記号で視覚的に表示する。

    Args:
        maze (list[list[int]]): 2次元配列の迷路。
            0=道, 1=壁, 8=スタート, 9=ゴール。
    """
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


def main():
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


if __name__ == "__main__":
    main()
    