# 同一の要素「i」がj個並んだリストを作成する
# @i 要素とする値
# @j int 要素数
def make_list_in_i(i, j):
    result = [i]*j
    return result

list1 = make_list_in_i(0, 9)
list2 = make_list_in_i('t', 9)

# iからjまでの数値を要素としたリストを作成する
def make_list_stairs(i, j):
    result =[x for x in range(i, j)]
    return result

list3 = make_list_stairs(2, 9)