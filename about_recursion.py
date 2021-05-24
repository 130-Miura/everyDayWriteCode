# 再帰を利用してnまでの総和を求める
def total(n):
    if n < 1:
        return 0
    return n + total(n - 1)

print(total(5))