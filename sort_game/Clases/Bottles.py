import random
class Bottles:
    def __init__(self, num) -> None:
        # 生成元
        self.origin = []
        for i in range(1, num - 1):
            for j in range(4):
                self.origin.append(i)
        # カラーボトル生成
        self.value = []
        for i in range(num-2):
            bottle = random.sample(self.origin, 4)
            self.value.append(bottle)
            for i in range(4):
                self.origin.remove(bottle[i])
        # 空ボトル生成
        self.value.append([0,0,0,0])
        self.value.append([0,0,0,0])

    
    def move(self, before, after):
        # 入れる場所があるか確認
        if 0 in self.value[after]:
            # 持ち上げる水の位置を取得
            for i in range(4):
                if self.value[before][i] != 0:
                    take_index = i
                    break
            # 入れる位置の取得
            for i in range(3, -1, -1):
                if self.value[after][i] == 0:
                    empty_index = i
                    break

            # 水の移動(条件：最大4回まで)
            while take_index < 4:
                # ボトルが空か同じ色の時だけ
                if empty_index == 3 or self.value[after][empty_index+1] == self.value[before][take_index]:
                    # 移動
                    self.value[after][empty_index] = self.value[before][take_index]
                    self.value[before][take_index] = 0
                    # ループ処理
                    take_index += 1
                    empty_index -= 1
                else:
                    break
    
    def clear_check(self):
        for i in range(len(self.value)):
            