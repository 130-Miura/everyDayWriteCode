# import time
# def time_check(func):
#     start = time.time()
#     func()
#     end = time.time()
#     print(end - start)

# list()にtarget以外の要素があるかどうかの確認は、set()にして減算することで確認できる
arr = ['abc', 'def', 'ghij', 'klmno']
target = ['abc', 'ghij', 'kk']
# print(set(arr) - set(['abc', 'ghij']))
# print(bool(set(arr) - set(['abc', 'ghij'])))


def use_set(arr, target):
    print(bool(set(arr) - set(target)))

use_set(arr, target)

