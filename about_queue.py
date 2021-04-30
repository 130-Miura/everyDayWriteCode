# queueモジュールは3種類
# キューから取り出されるエントリの順番だけが異なる
# FIFOキュー：最初に追加されたエントリが最初に取り出される
# LIFOキュー：最後に追加されたエントリが最初に取り出される
# 優先順位付きキューはエントリはheapqモジュールを利用してソートされ、最も低い値のエントリが最初に取り出される
# 内部的には3種類のキューは競争スレッドを一時的にブロックするためにロックを利用している
# スレッド内での再入を扱うようには設計されていない

# queue.Queue(maxsize=0)
# FIFOキューのコンストラクタ
# maxsizeはキューに入れられる要素の上限
# この大きさに達したら、キューの要素が減るまで挿入処理がブロックされる
# maxsizeが0以下ならキューの要素数は無限

# queue.LifoQueue(maxsize=0)
# LIFOキューのコンストラクタ

# queue.PriorityQueue(maxsize=0)
# 優先順位付きキューのコンストラクタ
# 最小の値を持つ要素が最初に検索される
# 最小の値はsorted(list(entries))[0]で返されるもの

# queue.SimpleQueue
# 無制限のFIFOキューのコンストラクタ
# タスク追跡などの機能を持たない
# バージョン3.7で追加された

# キューオブジェクトは以下のpublicメソッドを提供している
# Queue.qsize()
# キューの近似サイズを返す

# Queue.empty()
# キューが空の場合はTrueを返し、そうでなければFalseを返す

# Queue.full()
# キューがいっぱいの場合はTrueを返し、そうでなければFalseを返す

# Queue.put(item, block=True, timeout=None)
# itemをキューに入れる。blockがTrueでtimeoutがNoneの場合、フリースロットが利用可能になるまでブロックする
# timeoutが正の整数の場合、最大でtimeout秒間ブロックし、その時間内に空きスロットが利用可能にならなければ例外Fullを送出する
# blockがFalseの場合、空きスロットがすぐ利用できるならキューにitemを置き、利用できないなら例外Fullを送出する（timeoutは無視される）

# Queue.put_nowait(item)
# put(item, False)と同義

# Queue.get(block=True, timeout=None)
# キューからitemを取り除き、それを返す
# blockがTrueでtimeoutがNoneの場合、itemが取り出せるようになるまでブロックする
# timeoutが正の整数の場合、timeout秒間ブロックし、その時間内でitemが取り出せるようにならなければ例外Emptyを送出する
# blockがFalseの場合、itemがすぐ取り出せるならそれを返し、取り出せないなら例外Emptyを送出する（timeoutは無視される）

# Queue.get_nowait()
# get(False)と同義

import queue
# q = queue.Queue()
# q = queue.LifoQueue()
# q = queue.PriorityQueue()

# for i in range(5):
#     q.put(i)
#     q.put(3)

# while not q.empty():
#     a = q.get()
#     print(a)

# print(q.full())
# print(not q.full())

# q = queue.Queue(maxsize=2)
# for i in range(1, 4):
#     try:
#         q.put(i, timeout=2)
#     except queue.Full:
#         print(i)
