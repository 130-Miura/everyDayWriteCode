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

# formatメソッドで書式設定を行う
# 置き換えフィールドを含む文字列.format(値, 値, 値...)
# 複数の書式指定子がある
# print("名前は{2}です。年齢は{1}歳です。趣味は{0}です".format("tarou", 28, "ネットサーフィン"))

# 今日の日付を取得して、今日の日付を含んだファイル名を作成する
# from datetime import datetime 
# today = datetime.now().strftime("%Y%m%d")
# year = datetime.now().strftime("%Y")
# month = datetime.now().strftime("%m")
# day = datetime.now().strftime("%d")
# print(today)
# print(year)
# print(month)
# print(day)
# l = [year, month, day]

# print("file_{}.txt".format(today))
# print("file_{}_{}_{}.txt".format(year, month, day))

# setは変更可能、frozensetは変更不可能なセット
# 要素は重複しない
# 集合演算ができる
# 要素に変更可能なオブジェクトは指定不可
# a = set([1, 3, 5])
# b = frozenset([1, 3, 5])
# c = set()
# d = frozenset()
# print(a)
# print(b)
# print(c)
# print(d)

# a = 3
# b = set(a)
# print(b)

# a = set([1, 3, 5])
# b = set([2, 3, 8])
# c = set([1, 3, 5, 8])
# d = set([1, 3])

# 和集合
# print(a | b)

# 積集合
# print(a & b)

# 差集合
# print(a - b)
# print(b - a)

# 対称差集合
# print(a ^ b)

# 部分集合か判定
# print(a.issubset(b))
# print(a.issubset(c))
# print(a.issubset(d))

# 上位集合か判定
# print(a.issuperset(c))
# print(a.issuperset(d))

# getattr(object,name[,default])
# objectはクラス名、nameは取得する属性(変数)名、defaultは指定した属性が存在しなかった場合に返す値
# class a:
#     def __init__(self):
#         self.x = 1
#         self.y = 2
#     def plus(self):
#         return self.x + self.y
#     def minus(self):
#         return self.y - self.x
#     def hello(self, z):
#         return "hello " + z

# b = a()
# print(getattr(b, 'x'))
# print(getattr(b, 'y'))
# print(getattr(b, 'plus')())
# print(getattr(b, 'minus')())
# print(getattr(b, 'hello')('tarou'))

# getattrはオブジェクトの指定された属性の値を返す。
# もしその属性が存在しない場合、AttributeErrorを返す。
# hasattrはgetattrがAttributeErrorを返すかどうかを見て属性が存在するかどうかを返す関数。

# b = a()
# print(hasattr(b, 'x'))
# print(hasattr(b, 'y'))
# print(hasattr(b, 'plus'))
# print(hasattr(b, 'minus'))
# print(hasattr(b, 'hello'))

# hash(object)はオブジェクトのハッシュ値を返す。
# ハッシュ値は整数。辞書のキーを高速に検索する場合に使われる。
# print(hash('abc'))
# print(hash('abc'))
# print(hash(123))
# print(hash(123))
# print(hash('bca'))
