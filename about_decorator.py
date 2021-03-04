# デコレータについて
# 参考：https://qiita.com/_rdtr/items/d3bc1a8d4b7eb375c368

def a():
    print('hello')

# pythonでは関数を作るとそれぞれがスコープを持つ
# ＝関数がそれぞれ名前空間を持つ

# localな名前空間の値を辞書形式で返す
# print(locals())

# globalな名前空間の値を辞書形式で返す
# print(globals())

# ローカルに変数がない場合、グローバルな変数を探しに行く
text = 'test text'
# def b():
#     print(text)
# b()

# グローバルな変数を探しに行くが、変更はできない
# global変数を利用すると明示的に書くことで変更は可能
# def c():
#     global text
#     text = 'tes'
# c()
# print(text)

# 関数定義時につけたパラメータがローカル変数名になる
# def d(x=None):
#     print(locals())
# d()

# デフォルト値を渡すと任意の引数(デフォルトパラメータ)、渡さないと必須の引数(必須パラメータ)となる
# 必須の引数を関数呼び出し時に渡さないとTypeErrorが発生する
# def f(x, y=None):
#     print(x)
# f(6)

# pythonでは関数もオブジェクトのひとつでしかないので
# 関数に引数として渡したり、関数の戻り値として使うことができる
# def g():
#     return 1

# def h():
#     return 2

# def add(x, y):
#     print(x + y)

# add(g(), h())

# def i(x):
#     return x
# print(i(h()))

# この場合、y関数でreturnしていないため、fにはNoneが代入される
# def j():
#     x = 1
#     def y(a):
#         print(a)
#     return y(x)
# f = j()
# # print(f.keys())
# print(f)

# デコレータは関数を引数にとり、新たな関数を返すcallable
# callableとは引数をとって結果を返すオブジェクトの総称
# function,class,method,generatorもcallable
# def k(some_func):
#     def l():
#         print('print test')
#         ret = some_func()
#         return ret + 1
#     return l()
# def m():
#     return 1
# n = k(m)
# print(n)

# デコレータは以下のように呼ばれることが多いらしい
# m = k(m)

# デコレータの使用例
# class Coordinate(object):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __repr__(self):
#         return "Coord: " + str(self.__dict__)

# one = Coordinate(100, 200)
# two = Coordinate(300, 200)
# three = Coordinate(-100, -100)

# def wrapper(func):
#      def checker(a, b):
#          if a.x < 0 or a.y < 0:
#              a = Coordinate(a.x if a.x > 0 else 0, a.y if a.y > 0 else 0)
#          if b.x < 0 or b.y < 0:
#              b = Coordinate(b.x if b.x > 0 else 0, b.y if b.y > 0 else 0)
#          ret = func(a, b)
#          if ret.x < 0 or ret.y < 0:
#              ret = Coordinate(ret.x if ret.x > 0 else 0, ret.y if ret.y > 0 else 0)
#          return ret
#      return checker

# # add = wrapper(add)と同義
# @decorator名というシンタックスシュガーを利用するとadd関数をwrapperデコレータに渡したのと同じ意味になる
# シンタックスシュガー＝書き方を省略して簡単にしたもの
# @wrapper
# def add(a, b)
#     return Coordinate(a.x + b.x, a.y + b.y)

# # sub = wrapper(sub)と同義
# @wrapper
# def sub(a, b):
#     return Coordinate(a.x - b.x, a.y - b.y)

# print(sub(one, two))
# print(add(one, three))