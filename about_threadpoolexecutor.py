# import time
# import threading

# def boil_udon():
#   print('  うどんを茹でます。')
#   time.sleep(3)
#   print('  うどんが茹であがりました。')

# def make_tuyu():
#   print('  ツユをつくります。')
#   time.sleep(2)
#   print('  ツユができました。')

# print('うどんを作ります。')
# thread1 = threading.Thread(target=boil_udon)
# thread2 = threading.Thread(target=make_tuyu)
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# print('盛り付けます。')
# print('うどんができました。')

# from concurrent.futures import ThreadPoolExecutor
# import time

# def boil_udon():
#   print('  うどんを茹でます。')
#   time.sleep(3)
#   print('  うどんが茹であがりました。')

# tpe = ThreadPoolExecutor(max_workers=3)

# print('うどんを100個茹でます。')
# for _ in range(100):
#     tpe.submit(boil_udon)

# tpe.shutdown()
# print('うどんが100個茹で上がりました。')

# 以下の文はfeature.cancel()でキャンセルできずにFalseとなる
# feature変数に入っているのはExecutor.submit()で返されたFetureクラスのインスタンス
# 別の記事で、スレッドの実行中はキャンセルできないが、processpoolを使えばキャンセル可能って書いていた
# import time
# from concurrent.futures import ThreadPoolExecutor

# def foo():
#     time.sleep(3)
#     print('a')
#     time.sleep(5)
#     print('b')
#     return 'fooo'

# with ThreadPoolExecutor() as executor:
#     feature = executor.submit(foo)
#     print(type(feature))
#     print(feature.running())
#     print(feature.done())
#     print(feature.cancel())
#     print(feature.running())
#     print(feature.done())
#     time.sleep(4)
#     print(feature.cancel())
#     print(feature.running())
#     print(feature.done())
#     print(feature.cancelled())

# Executorクラスはインスタンス化されていない基底クラス
# ThreadPoolExecutorとProcessPoolExecutorの2つのサブクラスを持つ
# ThreadPoolExecutor：スレッドプールを指定して非同期処理を行う
# ProcessPoolExecutor：プロセスプールを指定して非同期処理を行う
# これらのサブクラスはExecutorクラスで定義された3つのメソッドが利用可能
# submit(fn, *args, **kwargs)
# 呼び出し可能オブジェクトfnをfn(*args, **kwargs)として実行するようにスケジュールし、
# Futureオブジェクト（呼び出し可能オブジェクトfnの非同期実行をカプセル化したもの）を返す
# map(func, *iterables, timeout=None, chunksize=1)
# *iterablesの要素をひとつずつfuncの引数として渡して実行する
# shutdown(wait=True)
# executorに対して、現在保留中のすべてのFutureが実行された後で、資源を解放するように伝える
# waitがTrueの場合、すべての未完了のFutureが完了してExecutorに関連づいたリソースが解放されるまで、このメソッドはreturnしない
# waitがFalseの場合、このメソッドはすぐにreturnし、すべての未完了のFutureが実行完了したときに、Executorに関連づいたリソースが解放される
# すべての未完了のFutureが実行完了するまでpythonプログラム全体は終了しない
