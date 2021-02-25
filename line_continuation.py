a = True
b = True
c = True
d = True
e = True
f = True
g = True
if a == True and b == True and c == True \
and d == True:
    print('ok')

# () [] {} 三重クオートなど非明示的な継続行が発生する場合を除き、
# 途中で改行するとSyntaxErrorが発生する
# 改行が必要な場合、\を行末に追加することで回避できる