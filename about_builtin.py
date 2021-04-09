# 組み込み関数の列挙
# print(list(name for name in vars(__builtins__)))

# 組み込み関数の種類（int()など、コンストラクタ含む）
# print(list(name for name in vars(__builtins__) if (name[0].islower() and name not in ('quit', 'exit', 'copyright', 'credits', 'license',)) or name == '__import__'))

# 組み込み関数の個数（int()など、コンストラクタ含む）
# print(len(list(name for name in vars(__builtins__) if (name[0].islower() and name not in ('quit', 'exit', 'copyright', 'credits', 'license',)) or name=='__import__')))

# all() 要素内の全てがTrueならTrueを返す
# a = 0
# l = [a < 8, -6 < a, 7, not False, True]
# if all(l):
#     print('リスト内の要素(式の結果)は全てTrue')

# any() 要素内のいずれかがTrueならTrueを返す
# a = 0
# l = [a < 8, -6 < a, 7, not False, True, False]
# if any(l):
#     print('リスト内の要素(式の結果)のいずれかがTrue')

# a = ['a', 'b', 2]
# breakpoint()

# 関数、メソッド、クラスは呼び出し可能
# print(callable(list()))
# print(callable(dict()))
# print(callable('a'))
# print(callable(3))
# def a():
#     pass

# print(callable(a))
# print(callable(a()))

# class A:
#     def b():
#         pass

# print(callable(A))
# print(callable(A()))
# print(callable(A.b))

# chr() Unicodeコードポイントが指定した整数である文字列を返す
# ord() 1文字のUnicode文字を表す文字列に対してUnicodeコードポイントを表す整数を返す
# print(ord('a'))
# print(chr(97))

# クラスメソッドのメリットは、外部ファイルのクラスをimportした際に
# その内部に持っているクラスメソッドが一緒にimportされること
# メソッドと違って、インスタンス化しなくても、クラスから直接呼び出し可能なこと

# class A:
#     @classmethod
#     def a(cls):
#         print(cls)
# A.a()

# あれ？インスタンス化しなくてもメソッド呼び出せてる...?
# いや、変数渡してる時点でインスタンス化してるのか
# class B:
#     def b(self):
#         print(self)
# B.b('test')

# dir()の引数がclassの時、メタ属性は含まれない
# print(dir())
# import struct
# print(dir())
# print(dir(struct))

# l = ['one', 'two', 'three', 'four']
# l = tuple(enumerate(l))
# l = dict(enumerate(l))
# l = list(enumerate(l))
# print(l)

# divmod()
# 第一引数と第二引数の商と剰余をタプルで返す
# print(divmod(5, 3))
# print(divmod(2.5, 2))
# print(divmod(10.5, 3.2))


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

# evalは第一引数に渡した式を評価し、評価した結果を返す
# execは第一引数に渡した文を評価し、Noneを返す（＝何も返さない）

# これは文なのでエラー
# eval('a = 3 + 2')

# eval,execともに第二引数にグローバル、第三引数にローカルな名前空間を渡せる

# eval('print(a)', {}, {'a': 2 + 3})
# exec('print(a)', {'a': 2 + 3}, {})

# evalは式の評価をするので名前空間の値を変更できない
# execは名前空間の値を変更できる

# a = {}
# exec('b = 5', {}, a)
# print(a)

# filter関数は第一引数に関数、第二引数にiterableをとる。
# 第二引数のiterableの値を順に関数の引数に渡して、Trueの場合のみ返す。
# l = list(filter(lambda x: x > 10, [2, 50, 3, 100, 25]))
# print(l)

# l = list(filter(lambda x: False, [2, 3, 10, 2]))
# print(l)