# 二分探索

# 二分探索を利用して目的の数値が格納してある、リストの引数を返す
# @numbers_list 数値を格納したリスト
# @target 探したい数値
# @return 目的の数値が格納された引数、または-1
def binary_search(numbers_list, target):

    # リストの中身を昇順に並べ替え
    l = sorted(numbers_list)

    left = 0
    right = len(l) - 1

    while left <= right:
        middle = (right + left) // 2

        # 中間にある数値を目的の数値を比較し、等しければその数値を返す
        if target == l[middle]:
            return middle

        if target < l[middle]:
            right = middle - 1

        if target > l[middle]:
            left = middle + 1

    # 目的の数値が発見できずに繰り返しを終了した場合、-1を返す
    return -1

l = [1, 4, 2, 5, 6, 9, 10, 11, 12, 13]

result = binary_search(l, 9)
if result >= 0:
    print(f'{result}番目の引数が目的の数値です')
else:
    print(f'目的の数値はありません')