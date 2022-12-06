import sys , random
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
    (px, py) = (WIDTH/2, HEIGHT/2)

    # スクリーン設定
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pygame_test")
    # 画像取得
    bg_img = pygame.image.load("./images/aozora.jpg").convert()
    bg_img_rect = bg_img.get_rect()
    player_img = pygame.image.load("./images/hiyoko.png").convert_alpha()
    player_img_rect = player_img.get_rect()
    player_img_rect.center = (px, py)

    while True:
        # スクリーン描写
        screen.fill(WHITE)
        screen.blit(bg_img, bg_img_rect)
        screen.blit(player_img, player_img_rect)
        # スクリーン更新
        pygame.time.wait(30)
        pygame.display.update()

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
