# 文字数ごとにグループ化

data = ['a', 'ab', 'c', 'abc', 'def', 'ghi', 'jk']

# 文字数ごとにグループ化する
# @data 異なる文字数の文字列を要素として持つリスト
# @return 要素を文字数ごとにグループ化したdict
def Group_by_number_of_characters(data):
    result = {}
    for x in data:
        l = len(x)

        # keyが存在する場合
        if l in result:
            result[l].append(x)

        # keyが存在しない場合
        else:
            result[l] = [x]
    return result

# print(f'グループ化の結果： {Group_by_number_of_characters(data)}')


# defaultdictを利用
from collections import defaultdict

# 文字数ごとにグループ化する
# @data 異なる文字数の文字列を要素として持つリスト
# @return 要素を文字数ごとにグループ化したdict
def group_by_defaultdict(data):
    result = defaultdict(list)
    for x in data:
        l = len(x)

        # keyが存在しない場合、自動でkeyを追加
        result[l].append(x)
    return result

# print(f'グループ化の結果： {group_by_defaultdict(data)}')