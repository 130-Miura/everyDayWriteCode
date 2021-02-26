# バブルソート
# @arr list 並び変えたい数値が格納されたリスト
# @asc_or_desk int 0の場合は昇順、1の場合は降順で並び変える。それ以外の値を渡すと並び返せずに返す
# @return list 並び変え後のリスト
def bubble_sort(arr, asc_or_desk=0):
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) - i - 1):
            if asc_or_desk == 0:
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
            elif asc_or_desk == 1:
                if arr[j] < arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
            else:
                return arr
    return arr

arr = [3, 8, 1, 2, 9]
print(bubble_sort(arr))

arr = [3, 8, 1, 2, 9]
print(bubble_sort(arr, 3))