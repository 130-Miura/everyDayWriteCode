import inspect
def is_generator():
    yield 1
    yield 2

def is_not_generator():
    return 1

# isgeneratorfunction()は、ジェネレータかどうかを調べる関数
# print(inspect.isgeneratorfunction(is_generator))
# print(inspect.isgeneratorfunction(is_not_generator))

# g = is_generator()
# print(inspect.getgeneratorstate(g))
# print(next(g))
# print(inspect.getgeneratorstate(g))
# print(next(g))
# print(inspect.getgeneratorstate(g))
# try:
#     print(next(g))
# except StopIteration as e:
    # スタック情報を表示する
    # import traceback
    # traceback.print_exc()

    # 現在処理中の例外を参照する
    # import sys
    # print(sys.exc_info())
    # print(inspect.getgeneratorstate(g))