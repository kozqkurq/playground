import pygame
import random

# 初期化
pygame.init()
WIDTH, HEIGHT = 400, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")

# ゲームボードを初期化
board = [[0] * 4 for _ in range(4)]

# 新しいランダムな2または4のブロックを生成する関数
def spawn_block():
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = 2 if random.random() < 0.9 else 4

# ゲームループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ブロックを描画
    for i in range(4):
        for j in range(4):
            pygame.draw.rect(win, (255, 255, 255), (i * 100, j * 100, 100, 100))
            if board[i][j] != 0:
                pygame.draw.rect(win, (255, 0, 0), (i * 100 + 5, j * 100 + 5, 90, 90))
                font = pygame.font.Font(None, 36)
                text = font.render(str(board[i][j]), True, (255, 255, 255))
                win.blit(text, (i * 100 + 35, j * 100 + 35))

    # ゲームロジックをここに追加

    pygame.display.update()

# ゲームが終了したらpygameを終了
pygame.quit()



for y in range(2, -1, -1):
    print(y)

x = 0
for y in range(4):
    
    while x < 4:
        print(x)
        x+=1
    