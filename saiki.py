# 再帰関数を利用して1~nまでの和を求める
# def saiki(n):
#     if n <= 0:
#         return 0
#     print(n)
#     return n + saiki(n-1)

# print(saiki(10))

import json

def search(arg, cond):
    res =[]
    if cond(arg):
        res.append(arg)
    if isinstance(arg, list):
        for item in arg:
            res += search(item, cond)
    elif isinstance(arg, dict):
        for value in arg.values():
            res += search(value, cond)
    return res

def has_star_key(arg):
    if isinstance(arg, dict):
        return arg.keys() == {"Deneb", "Altair", "Vega"}

def get_star(arg):
    return search(arg, has_star_key)

# importで実行までされないようにする
if __name__ == "__main__":

    # with句は__enter__メソッドと__exit__メソッドが定義されているクラスで利用可能
    # ブロックを抜ける際に__exit__メソッドであらかじめ登録された処理が実行される
    # 今回の場合、ブロックを抜ける際にファイルをclose()するため、エラーが発生しない
    with open('daisankaku.json', encoding='utf-8') as f:
        data = json.load(f)
        print(get_star(data))