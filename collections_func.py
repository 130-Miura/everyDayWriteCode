# Counterの使用例
from collections import Counter
# arr = [2, 7, 9, 1, 2, 6, 9, 5]
# c = Counter(arr)
# print('要素の出現回数は')
# for k, v in c.items():
#     print(f'{k}が{v}回')

# moji = 'tatoebakonnnamojiretu'
# c = Counter(moji)
# for k, v in c.items():
#     print(f'{k}が{v}回')

# defaultdictの使用例
from collections import defaultdict
# d = defaultdict(int)
# print(d[2])

# d = defaultdict(lambda: 100)
# print(d[6])

# dequeの使用例
from collections import deque
# d = deque([1, 2, 3, 4])
# d.pop()
# d.popleft()
# print(d)
# d.appendleft(7)
# d.append(9)
# print(d)