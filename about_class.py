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

