import sys, random
import pygame
from pygame.locals import *

# 定数定義
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WIDTH = 400
HEIGHT = 400



# ゲームボードを初期化
board = [[0] * 4 for _ in range(4)]

running = True

# 新しいランダムな2または4のブロックを生成する関数
def spawn_block():
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = 2 if random.random() < 0.8 else 4
    else:
        return False

def merge():
    pass

def main():
    # 初期化
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    # スクリーン設定
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("2048")
    font_h1 = pygame.font.Font('./fonts/ipaexg.ttf', 55)

    spawn_block()
    spawn_block()
    # board[1][1] = 2
    
    # 画像取得(背景)
    # bg = pygame.image.load("./images/bg.jpg").convert()
    # bg_rect = bg.get_rect() 

    while True:
        # スクリーン描写
        screen.fill(WHITE)
        # screen.blit(bg, bg_rect)
        # グリッド描画
        for i in range(3):
            screen.fill(BLACK, ((i+1)*100, 0, 1, 400))
        for i in range(3):
            screen.fill(BLACK, (0, (i+1)*100, 400, 1))
    
        for y, row in enumerate(board):
            for x, value in enumerate(row):
                if value != 0:
                    value_txt = font_h1.render(f"{value}", True, BLACK)
                    tx_rec = value_txt.get_rect(center = (50+(x*100), 50+(y*100)))
                    screen.blit(value_txt, tx_rec)

        # クリア時処理

        # スクリーン更新
        pygame.time.wait(30)
        pygame.display.update()

        # イベント受け取り
        for event in pygame.event.get():

            
            # 終了処理
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:

                if event.key == K_UP:
                    moved = False
                    for y in range(1, 4):
                        for x in range(4):
                            if board[y][x] != 0:
                                stock_y = y
                                while (y > 0 and board[y-1][x] == 0) or (y > 0 and board[y-1][x] == board[y][x]):
                                    moved = True
                                    if board[y-1][x] == board[y][x]:
                                        board[y-1][x] += board[y-1][x]
                                        board[y][x] = 0
                                        break
                                    else:
                                        board[y-1][x] = board[y][x]
                                        board[y][x] = 0
                                        y -= 1
                                      
                                y = stock_y

                    if moved:
                        spawn_block()

                if event.key == K_DOWN:
                    moved = False
                    for y in range(2, -1, -1):
                        for x in range(4):
                            if board[y][x] != 0:
                                stock_y = y
                                
                                while (y < 3 and board[y+1][x] == 0) or (y < 3 and board[y+1][x] == board[y][x]):
                                    print("down", y, x)
                                    moved = True
                                    if board[y+1][x] == board[y][x]:
                                        board[y+1][x] = board[y+1][x]*2
                                        board[y][x] = 0
                                        break
                                    else:
                                        board[y+1][x] = board[y][x]
                                        board[y][x] = 0
                                        y += 1
                                y = stock_y
                    if moved:
                        spawn_block()

                if event.key == K_LEFT:
                    moved = False
                    for y in range(4):
                        for x in range(1, 4):
                            if board[y][x] != 0:
                                stock_x = x
                                while (x > 0 and board[y][x-1] == 0) or (x > 0 and board[y][x-1] == board[y][x]):
                                    moved = True
                                    if board[y][x-1] == board[y][x]:
                                        board[y][x-1] = board[y][x-1]*2
                                        board[y][x] = 0
                                        break
                                    else:
                                        board[y][x-1] = board[y][x]
                                        board[y][x] = 0
                                        x -= 1 
                                x = stock_x

                    if moved:
                        spawn_block()

                if event.key == K_RIGHT:
                    moved = False
                    for y in range(4):
                        for x in range(2, -1, -1):
                            if board[y][x] != 0:
                                stock_x = x
                                while (x < 3 and board[y][x+1] == 0) or (x < 3 and board[y][x+1] == board[y][x]):
                                    moved = True
                                    if board[y][x+1] == board[y][x]:
                                        board[y][x+1] = board[y][x+1]*2
                                        board[y][x] = 0
                                        break
                                    else:
                                        board[y][x+1] = board[y][x]
                                        board[y][x] = 0
                                        x += 1
                                x = stock_x

                    if moved:
                        spawn_block()
                    

                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                

if __name__ == "__main__":
    main()
