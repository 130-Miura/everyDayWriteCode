# n個の空のリストを要素とするリストを生成
# @return 生成されたリスト
def make_arr(n, arr=[]):
    for _ in range(0, n):
        arr.append([])
    return arr

# print(make_arr(5)))