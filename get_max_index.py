# 指定した値（target）以下の、基数(base)に対する最大の指数を返す
def get_max_index(base, target):
    
    result = 1
    n = base
    while n < target:
        n = n * base
        result += 1
    return result

# print(get_max_index(2, 10 ** 18))
assert get_max_index(2, 15) == 4