# クラスの定義
# クラス名は慣習的に大文字で始める
# class MyClass:
#     """A simple example class"""

#     def __init__(self):
#         self.name = ""

#     def getName(self):
#         return self.name

#     def setName(self, name):
#         self.name = name

# a = MyClass()
# a.setName("Tanaka")
# print a.getName()

# クラスはクラス変数とインスタンス変数を持てる
# インスタンス変数はコンストラクタで初期化する
# クラス変数は全てのインスタンスに共通する変数
# インスタンス変数はインスタンス独自の変数
# インスタンス変数が存在しない場合クラス変数を参照する

# pythonではprivateやprotectedなどのアクセス修飾子の実装がなく、
# クラス変数、インスタンス変数はともにどこからでも参照可能（public）となる
# メソッドもpublic

# アクセスを制限する方法としてアンダースコア（_）や（__）がある
# _ひとつは参照できるが慣習的に参照しないもので、
# _ふたつは参照制限がある（ただし、_クラス名.__変数名と変換されるだけで、参照しようと思えばできる）

# コンストラクタ__init__()
# インスタンスが生成された時に呼びだされる

# デストラクタ__del__()
# インスタンスが消滅した時に呼び出される
# class MyClass:
#     def __init__(self):
#         print("インスタンスが生成された")
#     def __del__(self):
#         print("インスタンスが消滅した")

# a = MyClass()
# del a

# # インスタンスを暗黙的に文字列に変換する__str__()
# class MyClass:
#     def __init__(self, name, food):
#         self.name = name
#         self.food = food

#     def __str__(self):
#         return self.name + " like " + self.food

# a = MyClass("Tarou", "sushi")
# print(a)

# サブクラスは継承元の親クラスの変数やメソッドを利用できる
# 親クラスのメソッドのオーバーライドも可能
# class MyClass:
#     hello = "hello"

# class MyClass2(MyClass):
#     def __init__(self, world):
#         self.world = world

#     def greet(self):
#         print(self.hello, self.world)

# a = MyClass2("Japan")
# a.greet()

# super()を利用して親クラスの参照制限のかかったコンストラクタなどを参照可能
# class MyClass1(object):
#     def __init__(self):
#        self.val1 = 123

# class MyClass2(MyClass1):
#     def __init__(self):
#         super(MyClass2, self).__init__()
#         self.val2 = 456

# a = MyClass2()
# print(a.val1)
# print(a.val2)

# print(MyClass2.__dict__)
# print(a.__dict__)

# python3系ではクラス定義時の()を省略できる
# 省略して、class クラス名:　と書いた場合でも実際はトップレベル（ルートクラス）のobjectが引数に渡されている
# class クラス名（object）:　と書いた場合と同じとなる
# 全てのクラスはobjectを継承している
# dir関数にオブジェクトを渡すとプロパティ名とメソッド名がリストで返ってくる

# class Myclass:
#     def __init__(self, a, b):
#         self.x = a
#         self.y = b

#     def tasu(self):
#         wa = self.x + self.y
#         self.wa = wa
#         return wa

#     def hiku(self):
#         sa = self.x - self.y
#         self.sa = sa
#         return sa

# def tasizan(a, b):
#     return a + b

# print(dir(Myclass))
# print('\n')
# print(dir(Myclass(3, 2)))
# print('\n')
# print(dir(tasizan(3, 5)))

# pythonのスコープは以下の4種類
# ローカルスコープ（関数の中）
# エンクロージングスコープ（内部関数から見た外部関数の中）
# グローバルスコープ（ファイルの中）、モジュールスコープ＝外部ファイルの中
# ビルトインスコープ（組み込み関数の中、予約語とは別）

# グローバルスコープ
# g = 1

# def a(b):
#     # aのローカルスコープ
#     # aaやaaaのエンクロージングスコープ
#     c = 3

    # def aa(bb):
    #     def aaa(bbb):

    #         # aaaのローカルスコープ
    #         ccc = 333
    #         print('this is aaa', locals())
    #         print('c:', c, 'cc:', cc, 'g:', g, 'gg:', gg)
    #     # aaのローカルスコープ
    #     # aaaのエンクロージングスコープ
    #     cc = 33
    #     print('this is aa', locals())
    #     aaa(222)
    # print('this is a', locals())
    # aa(22)

# グローバルスコープ
# gg = 11