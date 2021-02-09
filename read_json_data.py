# jsonデータの作成
# https://www.json-generator.com/を参照
# jsonデータの読み込み
# jsonデータの出力

import json

filename = 'customer_data_created_by_generator.json'

# 読み込み専用でファイルを開く
fd = open(filename, mode='r')

# jsonファイルをデコード
data = json.load(fd)

# ファイルを閉じる
fd.close()

for d in data:
    
    # index属性が3のデータのみ出力しfor文を抜ける
    if d['index'] == 3:
        print(d)
        break
