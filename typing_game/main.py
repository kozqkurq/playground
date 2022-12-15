import sys, random, re, pykakasi
import pygame
from pygame.locals import *

# 定数定義
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WIDTH = 800
HEIGHT = 534
TYPING_LIST = [K_a, K_b, K_c, K_d, K_e, K_f, K_g, K_h, K_i, K_j, K_k, K_l, K_m, K_n, K_o, K_p, K_q, K_r, K_s, K_t, K_u, K_v, K_v, K_w, K_x, K_y, K_z, K_COMMA, K_PERIOD, K_MINUS, K_0, K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9]


class Test():
    
    # 生成・初期化
    def __init__(self):
        kakasi = pykakasi.kakasi()
        # フォント設定
        self.tfont = pygame.font.Font('./fonts/ipaexg.ttf', 36)
        self.cfont = pygame.font.Font('./fonts/ipaexg.ttf', 80)
        # 変数初期化
        self.text = "コーヒー"
        self.done_text = ""
        self.ruby = Test.convertHepburn(self.text)
        self.kana = [kakasi.convert(self.text[i])[0]["hepburn"] for i in range(len(self.text))]
        self.done_ruby = ""
        self.miss = 0 

    # 表示用関数(問題)
    def disp(self, screen):
        self.text_rend = self.tfont.render(self.text, True, BLACK)
        self.text_rect = self.text_rend.get_rect()
        self.text_rect.center = (WIDTH/2, 150)
        screen.blit(self.text_rend, self.text_rect)
    # 表示用関数(ルビ)
    def rubyDisp(self, screen):
        self.done_ruby_rend = self.tfont.render(self.done_ruby, True, BLACK)
        self.done_ruby_rect = self.done_ruby_rend.get_rect()
        self.done_ruby_rect.center = (WIDTH/2, 100)
        screen.blit(self.done_ruby_rend, self.done_ruby_rect)
    # 表示用関数(ミス)
    def missDisp(self, screen):
        self.miss_text = self.cfont.render(f"Miss : {self.miss}", True, BLACK)
        self.miss_text_rect = self.miss_text.get_rect()
        self.miss_text_rect.center = (WIDTH/2, 450)
        screen.blit(self.miss_text, self.miss_text_rect)
    # 表示用関数(クリア)
    def clearDisp(self, screen):
        self.clear_text = self.cfont.render("Clear!!", True, BLACK)
        self.clear_text_rect = self.clear_text.get_rect()
        self.clear_text_rect.center = (WIDTH/2, 350)
        screen.blit(self.clear_text, self.clear_text_rect)

    # 判定用関数
    def judge(self, key):
        if pygame.key.name(key) == self.ruby[0]:
            self.done_ruby += self.ruby[0]
            self.ruby = re.sub(r'.', '', self.ruby, count = 1)
            if len(self.ruby) == 0:
                return True
        else:
            self.miss += 1

    # ローマ字変換関数
    @staticmethod
    def convertHepburn(text):
        kakasi = pykakasi.kakasi()
        converted = kakasi.convert(text)
        print(converted)
        ruby = ""
        for i in range(len(converted)):
            ruby += converted[i]["hepburn"]
            print(ruby)
        return ruby

def main():
    # 初期化
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    # スクリーン設定
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Typing Game")
    
    # 画像取得(背景)
    bg = pygame.image.load("./images/bg.jpg").convert()
    bg_rect = bg.get_rect()

    # 変数初期化
    test = Test()
    judge = False   
    

    while True:
        # スクリーン描写
        screen.fill(WHITE)  
        screen.blit(bg, bg_rect)
        test.disp(screen)   # 問題文字描写
        test.rubyDisp(screen)
        # print(test.ruby)
        # クリア時処理
        if judge:
            test.clearDisp(screen)
            test.missDisp(screen)
            print(test.kana)

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
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                # タイピング受け取り
                if event.key in TYPING_LIST:
                    judge = test.judge(event.key)

                

if __name__ == "__main__":
    main()