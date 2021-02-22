# 数値かどうかをチェックする

# 渡された文字列が数値のみで構成されているかを確認する
# @n string
# @return 0-9のみの文字列の場合はTrueを返し、
# 0-9以外が入っている、または文字列以外が渡された場合はFalseを返す
def check_number_or_not(n):
    # 型の確認
    if type(n) != str:
        return False

    # 数値変換した際にエラーが発生するかを確認
    try:
        n = int(n)
        return True
    except:
        return False

print(check_number_or_not('25829'))
print(check_number_or_not(25829))
print(check_number_or_not('2x5829'))

