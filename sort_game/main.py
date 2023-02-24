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

                

if __name__ == "__main__":
    main()