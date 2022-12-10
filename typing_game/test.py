import sys, random
import pygame
from pygame.locals import *

# 定数定義
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WIDTH = 600
HEIGHT = 400

def main():
    # 初期化
    pygame.init()
    
    # 変数定義
    (px, py) = (0, 0)

    # スクリーン設定
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pygame_test")

    # 画像取得(背景)
    bg = pygame.image.load("./images/aozora.jpg").convert()
    bg_rect = bg.get_rect()
    # 画像取得(プレイヤー)    
    player = pygame.image.load("./images/hiyoko.png").convert_alpha()
    player_rect = player.get_rect()
    player_rect.center = (px, py)

    while True:
        # スクリーン描写
        screen.fill(WHITE)
        screen.blit(bg, bg_rect)
        screen.blit(player, player_rect)
        # スクリーン更新
        pygame.time.wait(10)
        pygame.display.update()
        
        px += 1
        py += 1
        player_rect.center = (px, py)
        if px > WIDTH:
            px = 0
        if py > HEIGHT:
            py = 0

        # イベント受け取り
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()


if __name__ == "__main__":
    main()
    
