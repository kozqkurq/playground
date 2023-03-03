import sys, random
import pygame
from pygame.locals import *
from Clases.Bottles import Bottles

# 定数定義
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TRANSPARENT = (0,0,0,0) 
RED = (203,0,0)
BLUE = (50,101,255)
GREEN = (0,203,0)
GRAY = (101,101,101,128)
COLORS = (TRANSPARENT, RED, BLUE, GREEN)

WIDTH = 800
HEIGHT = 440

def main():
    # 初期化
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
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

    # ボトル生成
    btl_num = 5
    # bottles = Bottles(btl_num)
    
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
            screen.fill(RED, pygame.Rect(WIDTH/2-(46/2), HEIGHT/2-85, 46, 200).move(x,0))
            # ボトル描写
            screen.blit(btl_image, btl_image_rect.move(x,0))
            # 繰り返し処理
            k = 50/(harf-0.5)
            x += (k + 100)

        # デバッグ用中央線
        screen.fill(BLACK, (WIDTH/2, 0, 1, HEIGHT))

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
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                

if __name__ == "__main__":
    main()