def solve_maze(maze):
    """迷路の袋小路を繰り返し埋めるアルゴリズム

    3方向以上が壁（または境界外）に囲まれた通路マス(0)を壁(1)に変換する.
    変化がなくなるまで繰り返すことで,すべての袋小路を除去する.
    ※ 破壊的変更あり（in-place更新）.

    Parameters
    ----------
    maze : list[list[int]]
        迷路を表す2次元リスト.
        1=壁,0=通路,8=スタート,9=ゴール。

    Returns
    -------
    maze : list[list[int]]
        袋小路を壁で埋めた後の迷路.
    """
    # 行数
    rows = len(maze)
    # 列数
    cols = len(maze[0])

    # 上下左右の4方向ベクトル
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 迷路に変更がある限りループを継続
    updated = True

    while updated:
        # ループ開始時に更新フラグをリセット
        updated = False

        for y in range(rows):
            for x in range(cols):
                # 通路マス(0)のみを対象とする
                if maze[y][x] == 0:
                    # 壁カウントの変数をリセット
                    wall_count = 0

                    # 隣接する4マスの壁数をカウントする
                    for dy, dx in directions:
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < rows and 0 <= nx < cols:
                            if maze[ny][nx] == 1:
                                # 隣接マスが壁の場合
                                wall_count += 1
                        else:
                            # 迷路の範囲外は壁として扱う
                            wall_count += 1

                    # 3方向以上が壁なら袋小路と判定し，壁に変換する
                    if wall_count >= 3:
                        maze[y][x] = 1
                        updated = True  # 更新が発生したので次のループも継続

    return maze


def print_maze(maze):
    """迷路を全角文字でコンソールに出力する関数

    各セルの値を以下の全角文字に変換して表示する。
        1 → ■（壁），0 → □（通路），8 → Ｓ（スタート），9 → Ｇ（ゴール）

    Parameters
    ----------
    maze : list[list[int]]
        表示対象の迷路。
    """
    for row in maze:
        row_str = ""
        for cell in row:
            if cell == 1:
                row_str += "■ "
            elif cell == 0:
                row_str += "□ "
            elif cell == 8:
                row_str += "Ｓ "  # スタート地点
            elif cell == 9:
                row_str += "Ｇ "  # ゴール地点
        print(row_str)


def main():
    """迷路の初期状態を定義し，袋小路除去の前後を表示するエントリーポイント

    10×10 のグリッドを初期迷路として定義し，solve_maze による処理前後を
    それぞれコンソールに出力する。
    """
    # 10×10 の初期迷路（8=スタート，9=ゴール）
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
        [1, 1, 1, 1, 1, 1, 9, 1, 1, 1],
    ]

    print("--- 初期状態  ---")
    print_maze(initial_maze)

    # 袋小路をすべて壁で埋める（initial_maze を直接更新）
    result_maze = solve_maze(initial_maze)

    print("\n--- 全ての袋小路を埋めた結果 ---")
    print_maze(result_maze)


if __name__ == "__main__":
    main()