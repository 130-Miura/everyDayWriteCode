# デコレータの種類
# 1.引数なし、ラッパー関数を返さない
# 2.引数なし、ラッパー関数を返す
# 3.引数あり、ラッパー関数を返さない
# 4.引数あり、ラッパー関数を返す

# def A():
#     return 'test'

# print(A)は関数自体を出力
# print(A())は関数の実行結果を出力

# def a():
#     def b():
#         print('b')
#     return b

# print(a())
# print(a()())
# a()()

# a()はa() = b
# a()()はb()
# print(a()())を実行したときの
# Noneってなんだ？
# →a()内でreturnしてるb()内では、何もreturnしてないから
# a()()を包んだprint()の結果でNoneか

# def c(func):
#     return func

# def d(msg=None):
#     if msg:
#         print(msg)
#     return('d')

# d関数自体が出力される
# print(c(d))

# d関数の実行結果が出力される
# print(c(d()))

# d関数にtarouが渡される
# print(c(d)('tarou'))

# こちらも同じ結果になる
# 最初にd関数にtarouを渡すか、c関数 = d関数 とした後にtarouを渡すかの違い
# print(c(d('tarou')))

# def adult(func):
#     def checker(name, age, action):
#         if age >= 20:
#             func(name, age, action)
#         else:
#             print(f'{name}は{age}歳なので、未成年のため{action}不可')
#     return checker

# @adult
# def action(name, age, action):
#     print(f'{name}は{age}歳なので、成人のため{action}可能')

# action('tarou', 22, '飲酒')

# action('yumi', 19, '喫煙')
