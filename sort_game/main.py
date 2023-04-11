import sys, random
import pygame
from pygame.locals import *
from Clases.Bottles import Bottles

# 定数定義
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TRANSPARENT = (0,0,0,0) 
RED = (255,41,62)
BLUE = (48,179,255)
GREEN = (54,255,64)
ORANGE = (255,126,33)
YELLOW = (255,241,89)
BROWN = (54, 44, 40)
GRAY = (101,101,101,128)
COLORS = (TRANSPARENT, RED, BLUE, GREEN, ORANGE, YELLOW, BROWN)

WIDTH = 800
HEIGHT = 440

START = 0
PLAY = 1
CLEAR = 2

def start():
    btl_num = random.randint(5, 7)
    bottles = Bottles(btl_num)
    return bottles

def main():
    # 初期化
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.mouse.set_pos((WIDTH/2, HEIGHT/2))
    selected_now = False
    now = START

    # スクリーン設定
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sort")
    font_h1 = pygame.font.Font('./fonts/ipaexg.ttf', 55)
    font_h2 = pygame.font.Font('./fonts/ipaexg.ttf', 48)
    start_btn = pygame.Rect(0,0,200,120)
    start_btn.center = (WIDTH/2, HEIGHT/2+100)
    
    # 画像取得(背景)
    bg = pygame.image.load("./images/bg.png").convert()
    bg_rect = bg.get_rect()
    btl_image = pygame.image.load("./images/bottle5.png").convert()
    colorkey_bg = btl_image.get_at((0,0))
    btl_image.set_colorkey(colorkey_bg, RLEACCEL)
    btl_image_rect = btl_image.get_rect(center=(WIDTH/2, HEIGHT/2))
    btl_image_rects = []
    
    while True:
        # スクリーン描写 
        screen.blit(bg, bg_rect)

        # スタート画面
        if now == START:
            # タイトル
            title = font_h1.render("Water", True, RED)
            tx_rec = title.get_rect(center = (WIDTH/2-150, HEIGHT/2-100))
            screen.blit(title, tx_rec)
            title = font_h1.render("Sort", True, BLUE)
            tx_rec = title.get_rect(center = (WIDTH/2, HEIGHT/2-100))
            screen.blit(title, tx_rec)
            title = font_h1.render("Puzzle", True, YELLOW)
            tx_rec = title.get_rect(center = (WIDTH/2+150, HEIGHT/2-100))
            screen.blit(title, tx_rec)
            # スタートボタン
            pygame.draw.rect(screen, (234, 235, 237), start_btn)
            text_start = font_h2.render("START", True, BROWN)
            tx_rec = text_start.get_rect(center = (WIDTH/2, HEIGHT/2+100))
            screen.blit(text_start, tx_rec)

        # プレイ画面
        elif now == PLAY:
            # ボトル枠描写
            scr = pygame.Surface((650, 350), flags=pygame.SRCALPHA)
            scr.fill(GRAY)
            scr_rect = scr.get_rect(center=(WIDTH/2, HEIGHT/2))
            screen.blit(scr, scr_rect)

            # クリアチェック
            if bottles.clear_check():
                now = CLEAR
            else:
                # 水ボトル描写
                harf = len(bottles.value) / 2
                x = harf * -100
                for i in range(len(bottles.value)):
                    # 水描写
                    y = 0
                    for j in range(4):
                        water_rect_f = pygame.Rect(WIDTH/2-(44/2), HEIGHT/2-83, 44, 50)
                        water_scr = pygame.Surface((800, 440), flags=pygame.SRCALPHA)
                        water_scr.fill(COLORS[bottles.value[i][j]], water_rect_f.move(x,y))
                        water_scr_rect = water_scr.get_rect()
                        screen.blit(water_scr, water_scr_rect)
                        y += 50
                    # ボトル描写
                    if len(btl_image_rects) < len(bottles.value):
                        btl_image_rects.append(btl_image_rect.move(x,0))
                    screen.blit(btl_image, btl_image_rects[i])
                    # 繰り返し処理
                    k = 50/(harf-0.5)
                    x += (k + 100)

        # クリア画面
        elif now == CLEAR:
            pass

        # スクリーン更新
        pygame.time.wait(30)
        pygame.display.update()

        # イベント受け取り
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    (x, y) = pygame.mouse.get_pos()
                    # スタート画面時
                    if now == START:
                        if start_btn.collidepoint(x, y):
                            bottles = start()
                            now = PLAY
                    # プレイ画面時
                    elif now == PLAY:
                        for i in range(len(bottles.value)):
                            if (btl_image_rects[i].left+25 <= x <= btl_image_rects[i].left+75) and (95 <= y <= 345):
                                print("pow")
                                if selected_now and before != i:
                                    after = i
                                    bottles.move(before, after)
                                    selected_now = False
                                    print(bottles.value)
                                else:
                                    before = i
                                    selected_now = True


            # 終了処理
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                

if __name__ == "__main__":
    main()