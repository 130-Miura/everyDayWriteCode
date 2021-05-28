# 複数のリストの要素のうち、最大値を返す
# l = [1, 5, 9, 12, 3]
# ll = [3, 7, 2]
# print("max:", max(*l, *ll))
# print("min:", min(*l, *ll))

# 辞書のキー、または値の最大値を返す
# dd = {3: 9, 5: 1, 3: 123}
# print("max.key:", max(dd))
# print("max.values:", max(dd.values()))
# print("max.key:", min(dd))
# print("max.values:", min(dd.values()))

# l = ['a', 'bb', 'ccc', 'tt', 'aaaa', 'bbbbb', 'eee']
l = ['a', 'bb', 'ccc', 'tt', 'aaaa', 'bbbbb', 'eee', 'c']
def sort_by_len(l):
    d = {}
    for s in l:
        d[s] = len(s)
    # return max(d.values())
    # return min(d.items())
    v, k = max((v, k) for k, v in d.items())
    return (k, v)

print(sort_by_len(l))

