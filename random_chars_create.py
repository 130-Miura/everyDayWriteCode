# ランダムな文字列の生成
# a-z,A-Z,_を利用可
# 文字列の長さは指定できること

import random

# ランダムな指定長の文字列を生成する
# @length int 文字列の長さ
# @return str 生成された指定長のランダムな文字列
def random_str(length):

    # 文字列生成に利用する文字を指定
    chars = 'abcdefghijklmnopqrstuvwxzyABCDEFGHIJKLMNOPQRSTUVWXYZ_'

    # 指定された文字列の長さ分、ランダムに文字を生成して結合
    return ''.join([random.choice(chars) for _ in range(length)])

# 文字列の長さを指定（この例では1~10文字のいずれかをランダムで指定）
chars_length = random.randint(1, 10)
print(random_str(chars_length))