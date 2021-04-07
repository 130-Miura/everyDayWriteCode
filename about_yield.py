# yieldは関数を一時的に実行停止にできる文
# yieldはジェネレータを作れる
# def my_generator(x):
#     for i in range(x):
#         yield i

# x = my_generator(5)
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())

# 次回__next__が呼ばれるまでyieldの処理で一時停止される
# def gen1():
#     yield 1
#     yield 2
#     yield 3

# def gen2():
#     yield 4
#     yield 5
#     yield 6

# yield from ジェネレータでジェネレータをまとめて、順次実行できる
# def gen_mix(g1, g2):
#     yield from g1
#     yield from g2

# x = gen_mix(gen1(), gen2())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())

# __next__()とnext()は同義
# def gen():
#     yield 1
#     yield 2
#     yield 3

# x = gen()
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

# seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# print(list(enumerate(seasons)))
# print(list(enumerate(seasons, 1)))

# l = enumerate(seasons)
# print(l.__next__())
# print(l.__next__())
# print(l.__next__())
# print(l.__next__())
# print(l.__next__())

# eval関数は引数に渡された文字列をpythonコードとして評価する
# def func():
#     print('func() is called')

# global_val = 'this is global'

# 通常のグローバル関数、変数呼び出し
# func()
# print(global_val)

# 文字列からグローバル関数、変数呼び出し
# eval('func')()
# print(eval('global_val'))
