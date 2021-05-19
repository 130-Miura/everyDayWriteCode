from itertools import accumulate
from itertools import chain
# accumulate()は引数に渡したイテラブルの、その要素までの累積和を返す
print(list(accumulate([1, 5, 10])))
# chain(*iterable)は複数のイテラブルのすべての要素で中間リストを作成せずにそれぞれのイテラブルを処理する
print(list(accumulate(chain([1, 5, 10], [7, 4, 9]))))
