import pykakasi

kakasi = pykakasi.kakasi() # インスタンスの作成
print(kakasi.convert('ねこ')) # ねこをローマ字に変換する処理
print(kakasi.convert('')) # ネコをローマ字に変換する処理
print(kakasi.convert('行う')) # 猫をローマ字に変換する処理