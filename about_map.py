# map(function, iterable)
# iterableの要素をそれぞれfunctionに代入して処理する
# print(map(lambda x: x + 'zz', ['a', 'b', 'c']))
# print(list(map(lambda x: x + 'zz', ['a', 'b', 'c'])))

# l = ['a', 'b', 'c']

# def add_zzz(x):
#     return x + 'zzz'
# print(map(add_zzz, l))
# print(list(map(add_zzz, l)))

# l = [1, 5, 78, 201]

# def int_to_str(x):
#     return str(x)
# print(list(map(int_to_str, l)))