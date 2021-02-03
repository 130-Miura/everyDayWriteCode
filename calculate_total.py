# 1からnまでの整数の和を求める

# for文を利用して1~nまでの整数を合計
def total_using_iterative_syntax(n, result=0):
    for i in range(1, n+1):
        result += i
    return result

# print(total_using_iterative_syntax(3))

# sum関数を利用して1~nまでの整数を合計
def total_using_the_sum_function(n, arr=[]):
    for i in range(1, n+1):
        arr.append(i)
    return sum(arr)

# print(total_using_the_sum_function(11))

# 謎解き風に1~nまでの整数を合計
def mystery_solving_style(n):
    sum = int(n/2*(n+1))
    return sum

# print(mystery_solving_style(15))