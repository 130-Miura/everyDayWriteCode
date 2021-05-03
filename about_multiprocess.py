# from multiprocessing import Process
# import os

# def info(title):
#     print(title)
#     print('module name:', __name__)
#     print('parent process:', os.getppid())
#     print('process id:', os.getpid())

# def f(name):
#     info('function f')
#     print('hello', name)

# if __name__ == '__main__':
#     info('main line')
#     p = Process(target=f, args=('bob',))
#     p.start()
#     p.join()

# import multiprocessing as mp

# def foo(q):
#     q.put('hello')

# if __name__ == '__main__':
#     mp.set_start_method('spawn')
#     q = mp.Queue()
#     p = mp.Process(target=foo, args=(q,))
#     p.start()
#     print(q.get())
#     p.join()

# import multiprocessing as mp

# def foo(q):
#     q.put('hello')

# if __name__ == '__main__':
#     ctx = mp.get_context('spawn')
#     q = ctx.Queue()
#     p = ctx.Process(target=foo, args=(q,))
#     p.start()
#     print(q.get())
#     p.join()

# 複数スレッド下でもロックを持つ単一スレッドでしかバイトコードが実行できず、その他のスレッドは待機状態になる
from datetime import datetime
from threading import Thread
import time

# 対象：CPUバウンドな処理（CPUの計算速度に依存する処理）
# 結果：マルチスレッドを利用しても、単純に指定回数分の処理を繰り返しても、処理時間はほぼ同じだった
# CPUバウンドな処理はマルチスレッド機能を利用しても1スレッドずつしか実行されなかった
# ただ、単純に指定回数分の処理を繰り返す方の処理が始まると、CPUが音を上げる傾向があった（処理順を逆にしても同様）
# def countdown():
#     n = 10000000
#     while n > 0:
#         n -= 1

# if __name__ == '__main__':
#     t1 = Thread(target=countdown)
#     t2 = Thread(target=countdown)
#     t3 = Thread(target=countdown)
#     t4 = Thread(target=countdown)
#     t5 = Thread(target=countdown)

# それぞれのスレッドで処理を1回ずつ実行する（5スレッド＝処理実行回数は計5回）
    # start = datetime.now()
    # t1.start()
    # t2.start()
    # t3.start()
    # t4.start()
    # t5.start()
    # t1.join()
    # t2.join()
    # t3.join()
    # t4.join()
    # t5.join()
    # end = datetime.now()
    # print(f"Time: {end - start}")

# 処理を単純に5回実行する（処理実行回数は計5回）
    # start = datetime.now()
    # for _ in range(5):
    #     countdown()
    # end = datetime.now()
    # print(f"Time: {end - start}")

# 対象：I/Oバウンドな処理（I/Oの入出力に依存する処理）
# 結果：n回処理を繰り返す際、処理総時間が1/nとなった
# I/Oバウンドな処理はマルチスレッドによって並行処理された
# def sleep():
#     time.sleep(2.0)

# if __name__ == '__main__':
#     t1 = Thread(target=sleep)
#     t2 = Thread(target=sleep)
#     t3 = Thread(target=sleep)
#     t4 = Thread(target=sleep)
#     t5 = Thread(target=sleep)

#     start = datetime.now()
#     t1.start()
#     t2.start()
#     t3.start()
#     t4.start()
#     t5.start()
#     t1.join()
#     t2.join()
#     t3.join()
#     t4.join()
#     t5.join()
#     end = datetime.now()
#     print(f"Time: {end - start}")

#     start = datetime.now()
#     for _ in range(5):
#         sleep()
#     end = datetime.now()
#     print(f"Time: {end - start}")