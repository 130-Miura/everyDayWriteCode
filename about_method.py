class Food(object):
    def __init__(self, food_name):
        self.food_name = food_name
    def get_food_name(self):
        return self.food_name

print(Food.get_food_name)
print(Food('apple').get_food_name())
f = Food('orange').get_food_name
print(f())

# バインドされているオブジェクトの確認
print(f.__self__)
print(f == f.__self__.get_food_name)

