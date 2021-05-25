# 複数のリストの要素のうち、最大値を返す
l = [1, 5, 9, 12, 3]
ll = [3, 7, 2]
print(max(*l, *ll))

# 辞書のキー、または値の最大値を返す
dd = {3: 9, 5: 1, 3: 123}
print(max(dd))
print(max(dd.values()))