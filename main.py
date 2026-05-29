def solve_maze(maze):
    rows = len(maze)
    cols = len(maze[0])
    
    # 上下左右の移動量を表すベクトル (dy, dx)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while True:
        updated = False  # この周回で書き換え（穴埋め）があったかのフラグ
        
        for y in range(rows):
            for x in range(cols):
                # 対象は「道(0)」のみ
                if maze[y][x] == 0:
                    wall_count = 0
                    
                    # 上下左右の4方向を検査
                    for dy, dx in directions:
                        ny, nx = y + dy, x + dx
                        
                        # 迷路の範囲内（インデックスアウトの防止）
                        if 0 <= ny < rows and 0 <= nx < cols:
                            # 隣が元の壁(1)か、既に埋められた袋小路(2)ならカウント
                            if maze[ny][nx] in (1, 2):
                                wall_count += 1
                    
                    # 3面以上が壁に囲まれていたら袋小路として埋める
                    if wall_count >= 3:
                        maze[y][x] = 2  # 灰色（2）に書き換え
                        updated = True   # 更新フラグを立てる
                        
        # 迷路全体を1周スキャンして、どこも書き換わらなくなったら終了（確定）
        if not updated:
            break
            
    return maze

def print_maze(maze):
    """迷路を視覚的に見やすく表示する関数"""
    for row in maze:
        row_str = ""
        for cell in row:
            if cell == 1:
                row_str += "■ "  # 元の壁
            elif cell == 2:
                row_str += "▤ "  # 穴埋めされた袋小路（図2の灰色）
            elif cell == 0:
                row_str += "□ "  # 残った正しい道
            elif cell == 8:
                row_str += "Ｓ " # スタート
            elif cell == 9:
                row_str += "Ｇ " # ゴール
        print(row_str)

# --- メイン処理 ---

# 【図3・拡大図】のデータを完全に再現した2次元配列 (0ベースインデックス)
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

# アルゴリズムの実行
result_maze = solve_maze(initial_maze)

print("\n--- 全ての袋小路を埋めた結果 (図2) ---")
print_maze(result_maze)