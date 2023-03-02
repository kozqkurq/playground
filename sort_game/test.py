bottle1 = [0, 0, 0, 0]
bottle2 = [1, 2, 1, 2]
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
        # 入れる位置の取得
        for i in range(3, -1, -1):
            if after_btl[i] == 0:
                empty_index = i
                break

        # 水の移動(条件：最大4回まで)
        while take_index < 4:
            # ボトルが空か同じ色の時だけ
            if empty_index == 3 or after_btl[empty_index+1] == before_btl[take_index]:
                # 移動
                after_btl[empty_index] = before_btl[take_index]
                before_btl[take_index] = 0
                # ループ処理
                take_index += 1
                empty_index -= 1
            else:
                break
    
            

move(bottle2, bottle1)
print(bottles)

move(bottle1, bottle2)
print(bottles)

# result = move(bottle3, bottle2)
# print(bottles)
# print(result)

# result = move(bottle3, bottle1)
# print(bottles)
# print(result)
# move(bottle3, bottle2)

