from collections import Counter
a = ['a', 'b', 'c', 'a', 'bb', 'c', 'd']
c = Counter(a)
print(c)

# collections.Counterは標準モジュールの一つ
# リストの要素ごとの出現数をカウントした結果を取得する
# 返り値のCounterクラスは辞書型のサブクラスのため、辞書型と同じ操作ができる
