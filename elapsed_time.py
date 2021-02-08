# 一連の処理にかかる時間を計測

import time

def test():
    for _ in range(0, 15):
        print('aabd')

# 関数の一連の処理による経過時間を計測
# @return 経過時間
def check_elapsed_time(func):
    start = time.time()

    # 計測したい処理
    func()

    # 処理終了時間 - 処理開始時間
    elapsed_time = time.time() - start
    return elapsed_time

print("経過時間:{0}".format(check_elapsed_time(test)) + "[秒]")