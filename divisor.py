# N個の数値が書いた玉A1～ANがある
# A1～ANから2つ選ぶ（B、Cとする）
# BとCの最大公約数、または最小値のどちらかが書かれた玉を追加する
# 最後の1つになるまで繰り返す
# 最後に残る可能性のある数値は何種類あるか

# 最初に与えられた数値の最小値をA_minに代入する
# 最大公約数になる可能性のある数値を総当たりで計算する
# それらをリスト化し、繰り返し文で総当たりを行い、
# 最大公約数になりうる数値をリストYakusuuに追加していく
# リストYakusuuの値のうち、A_minより小さい数値を数える
# その結果を出力する

from math import gcd

# resultに0を代入
# 総当たりで最大公約数になる数値をリスト化
# リスト化された数値の中で、A‗min以下の値があればresultをインクリメント
# resultを出力

N = 9
A = '28 79 46 31 43 57 85 92 96'
A = list(map(int, A.split()))
A_min = min(A)
ans = 0
Yakusuu = []

# 求めた最大公約数のうち、重複しない数値をリストYakusuuに追加
for i in range(N):
    I = i
    for n in range(I, N):
        yakusuu = gcd(A[i], A[n])
        if yakusuu not in Yakusuu:
            Yakusuu.append(yakusuu)

# リストYakusuuに追加された数値のうち、A_min以下の数値があればansをインクリメント
for i in range(len(Yakusuu)):
    if Yakusuu[i] <= A_min:
        ans += 1
print(ans)
