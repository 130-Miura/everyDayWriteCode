class MyClass:
    count = 0                       # クラス変数を初期化

    def __init__(self):
        MyClass.count += 1          # クラス変数をカウントアップ

a1 = MyClass()
a2 = MyClass()
print(MyClass.count)                 #=> 2