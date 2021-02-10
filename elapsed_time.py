# 一連の処理にかかる時間を計測

import time

def test():
    arr = []
    for _ in range(0, 15):
        arr.append('aaa')

# 関数の一連の処理による経過時間を計測
# @return 経過時間
def check_elapsed_time(func):
    start = time.time()

    # 計測したい処理
    func()

    # 処理終了時間 - 処理開始時間
    elapsed_time = time.time() - start
    return elapsed_time

# print("経過時間:{0}".format(check_elapsed_time(test)) + "[秒]")

# timeitライブラリを利用した処理時間の計測
import timeit
print(
    timeit.timeit(
        
        # 計測対象
        "test()"

        # グローバル読み込み
        , globals=globals()

        # 計算する処理回数
        , number=50000
    )
)