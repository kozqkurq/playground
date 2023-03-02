import sys, random
import pygame
from pygame.locals import *

# 定数定義
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WIDTH = 800
HEIGHT = 534

def main():
    # 初期化
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    # スクリーン設定
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("")
    
    # 画像取得(背景)
    # bg = pygame.image.load("./images/bg.jpg").convert()
    # bg_rect = bg.get_rect() 

    bottle1 = [0, 0, 0, 0]
    bottle2 = [1, 1, 2, 2]
    bottle3 = [2, 2, 1, 1]

    bottles = [bottle1, bottle2, bottle3]

    def move(before_btl, after_btl):
        # 入れる場所があるか確認
        if 0 in after_btl:
            # 持ち上げる水の位置を取得
            for i in range(4):
                if before_btl[i] != 0:
                    take_index = i
                    break
            take_water = before_btl[take_index]
            first_take = take_water
            # 水の移動
            while take_water == first_take:
                for i in range(3, -1, -1):
                    if after_btl[i] == 0:
                        empty_index = i
                        break
                after_btl[empty_index] = take_water
                before_btl[take_index] = 0

                take_index -= 1
                take_water = before_btl[take_index]


    while True:
        # スクリーン描写
        screen.fill(WHITE)  
        # screen.blit(bg, bg_rect)
        # クリア時処理

        screen.fill(BLACK, (WIDTH/2, 0, 1, 534))    # デバッグ用中央線

        # スクリーン更新
        pygame.time.wait(30)
        pygame.display.update()

        # イベント受け取り
        for event in pygame.event.get():

            # 終了処理
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

                

if __name__ == "__main__":
    main()