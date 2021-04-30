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
# 別の記事で、スレッドの実行中はキャンセルできないが、processpoolを使えばキャンセル可能って書いてた
# import time
# from concurrent.futures import ThreadPoolExecutor

# def foo():
#     time.sleep(3)
#     return 'fooo'

# with ThreadPoolExecutor() as executor:
#     feature = executor.submit(foo)
#     print(feature.running()) # True
#     print(feature.done()) # False
#     print(feature.cancel()) # 処理のキャンセル

#     print(feature.running()) # False
#     print(feature.done()) # True