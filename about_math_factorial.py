import math
# math.factorial()は階乗の計算結果を返す関数
# print(math.factorial(5))

# n個のボールからr個のボールを選択する組み合わせの数は以下の式で求められる
# n! // (r! * (n - r)!)

# 4個から3個とる組み合わせ
# print(math.factorial(4) // math.factorial(3) * math.factorial(4 - 3))

# 
# def return_combination(n, r):
#     return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

# print(return_combination(4, 3))
# print(return_combination(7, 3))
# print(return_combination(5, 2) * return_combination(2, 1))

