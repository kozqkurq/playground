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
GRAY = (101,101,101,128)
COLORS = (TRANSPARENT, RED, BLUE, GREEN, ORANGE, YELLOW)

WIDTH = 800
HEIGHT = 440

def main():
    # 初期化
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.mouse.set_pos((WIDTH/2, HEIGHT/2))
    selected_now = False
    # スクリーン設定
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sort")
    font = pygame.font.Font('./fonts/ipaexg.ttf', 36)
    
    # 画像取得(背景)
    bg = pygame.image.load("./images/bg.png").convert()
    bg_rect = bg.get_rect()
    btl_image = pygame.image.load("./images/bottle5.png").convert()
    colorkey_bg = btl_image.get_at((0,0))
    btl_image.set_colorkey(colorkey_bg, RLEACCEL)
    btl_image_rect = btl_image.get_rect(center=(WIDTH/2, HEIGHT/2))
    btl_image_rects = []

    # ボトル生成
    btl_num = 6
    bottles = Bottles(btl_num)
    print(bottles.value)
    
    while True:
        # スクリーン描写 
        screen.blit(bg, bg_rect)
        scr = pygame.Surface((650, 350), flags=pygame.SRCALPHA)
        scr.fill(GRAY)
        scr_rect = scr.get_rect(center=(WIDTH/2, HEIGHT/2))
        screen.blit(scr, scr_rect)

        # 水ボトル描写
        harf = btl_num / 2
        x = harf * -100
        for i in range(btl_num):
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
            if len(btl_image_rects) < btl_num:
                btl_image_rects.append(btl_image_rect.move(x,0))
            screen.blit(btl_image, btl_image_rects[i])
            # 繰り返し処理
            k = 50/(harf-0.5)
            x += (k + 100)

        # デバッグ用中央線
        # screen.fill(BLACK, (WIDTH/2, 0, 1, HEIGHT))


        # スクリーン更新
        pygame.time.wait(30)
        pygame.display.update()

        

        # イベント受け取り
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    x,y = event.pos
                    for i in range(btl_num):
                        if (btl_image_rects[i].left+25 <= x <= btl_image_rects[i].left+75) and (95 <= y <= 345):
                            if selected_now and before != i:
                                after = i
                                bottles.move(before, after)
                                selected_now = False
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