# 関数のカプセル化

def outer_func(number):

    # 内部関数を定義
    def inner_func():
        return number + 1

    # 内部関数の呼び出し
    return inner_func()

# 内部関数の外側の関数からは呼び出し可能
# print(outer_func(5))

# グローバルからは呼び出し不可で、NameErrorを返す
# print(inner_func(5))
