# べき乗した値の剰余を求める計算をする場合の、処理速度の差
# a ** bのaとbの数値が境界値より大きければgの関数が早く、
# 小さければf,hの関数が早い

def f(x):
    return x**53%3
def g(x):
    return pow(x, 53, mod=3)
def h(x):
    return pow(x, 53) % 3

import timeit
print(timeit.timeit('f(14)', globals=globals()))
print(timeit.timeit('g(14)', globals=globals()))
print(timeit.timeit('h(14)', globals=globals()))
print('')
print(timeit.timeit('f(142)', globals=globals()))
print(timeit.timeit('g(142)', globals=globals()))
print(timeit.timeit('h(142)', globals=globals()))