# 小文字の英文字が存在するか確認

import re
char = '666666t89'
pattern = r"([a-z])"
result = re.search(pattern, char)
if result != None:
    print('小文字の英文字を発見')
else:
    print('小文字の英文字を発見できず')