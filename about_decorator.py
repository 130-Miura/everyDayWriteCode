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

