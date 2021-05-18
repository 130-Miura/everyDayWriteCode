import math

# lambda 引数: 返り値

# def func(引数):
    # return 返り値

# 以下2つは同じ
# def double(n):
#     return n * 2
# print(double(7))

# l = lambda n: n * 2
# print(l(7))

# # 円の面積
# l = lambda n: n * n * 3.14
# print(l(7))

# 課税後の価格を求める
# price int 金額
# tax int 税金（％） 10%の場合省略可
# return 課税後の価格（端数切り捨て）
# def add_tax(price, tax=10):
#     return price + price * tax // 100
# print(add_tax(102))
# print(add_tax(100, 8))
# print(add_tax(1200, 8))
# print(add_tax(1545))

# l = lambda price, tax=10: price + price * tax // 100
# print(l(102))


# def take_tax(price, tax=10):
#     return math.floor(price / (100 + tax) * 100)
# print(take_tax(1296, 8))
# print(take_tax(1700))

# l = lambda price, tax=10: math.floor(price / (100 + tax) * 100)
# print(l(1700))

sample_list = [7, 20, 2]
l = lambda x, y: x * y
for x, y in enumerate(sample_list, 1):
    print(l(x, y))

sample_dict = {}
sample_list = ['a', 'b', 'c']
for x, y in enumerate(sample_list):
    sample_dict[x] = y
print(sample_dict)

sample_dict = {}
for x, y in enumerate(sample_list):
    sample_dict[y] = x