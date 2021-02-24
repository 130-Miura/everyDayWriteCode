# num_balls球の数値が書かれたボールがある
# targetの数値の書かれたボールを取り除いく
# 残ったボールを文字列、空白区切りで出力する
# ボールが残らない場合はから文字列を出力する

num_balls, target = map(int, '5 5'.split())
balls = list(map(int, '3 5 6 5 4'.split()))

# targetと一致しない数値をリストに追加
li = list(str(x) for x in balls if x != target)
# li = list(filter(lambda x:x != target, balls))

# 空白区切りでリストの中身を文字列化
if len(li) == 0:
    print('')
else:
    ans = ' '.join(li)
    print(ans)