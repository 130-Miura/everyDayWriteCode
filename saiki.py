# 再帰関数を利用して1~nまでの和を求める
def saiki(n):
    if n <= 0:
        return 0
    print(n)
    return n + saiki(n-1)

print(saiki(10))