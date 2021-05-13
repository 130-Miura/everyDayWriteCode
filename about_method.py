class Food(object):
    def __init__(self, food_name):
        self.food_name = food_name
    def get_food_name(self):
        return self.food_name
    # 静的メソッドの2つのメリット
    # self引数が必要ない場合に利用するとself引数がある場合と比べて早い
    # クラスオブジェクトの状態に依存しないことが一目で分かる
    @staticmethod
    def x_plus_y(x, y):
        return x + y

    a_dislike_food = 'パクチー'
    # クラスメソッドはクラスにバインドされる
    # __init__と異なるシグネチャを使ってオブジェクトをインスタンス化するファクトリメソッドが作成できる
    # 外部ファイルに記述してインポートして使う場合、
    # クラスメソッドとすることでクラスをインポートするだけでよくなる
    # そうでない場合、クラスと、クラスメソッドにしなかったその関数を呼び出す必要がある
    @classmethod
    def dislike_food(cls):
        return cls.a_dislike_food

    @classmethod
    def make_factory(cls, obj):
        return obj.x + obj.y

class x_and_y:
    def __init__(self, x, y):
        self.x = x
        self.y = y

inst = x_and_y(2, 8)

# print(Food.make_factory(inst))

# print(Food.get_food_name)
# print(Food('apple').get_food_name())
# f = Food('orange').get_food_name
# print(f())

# バインドされているオブジェクトの確認
# print(f.__self__)
# print(f == f.__self__.get_food_name)

# 静的メソッドはインスタンス化せず呼び出し可能
# print(Food.x_plus_y(2, 5))

# クラスメソッドもインスタンス化せず呼び出し可能。
# メソッドの引数にオブジェクトを渡してインスタンス化可能（ファクトリメソッド）
# print(Food.dislike_food(), 'が嫌いだ', sep='')
