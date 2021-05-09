from unittest import mock
# モックの作成
m = mock.Mock()

# モックにメソッドとメソッド呼び出し時の返り値を設定
# m.some_method.return_value = 50
# print(m.some_method())
# print(m.some_method(64, None))
def print_arg(arg):
    print(arg)
    return 50

# side_effect属性はモック呼び出し時の例外発生などの副作用を実行できる
m.method.side_effect = print_arg
print(m.method('tarou'))
m.method('satou')

# call_count属性はメソッドが呼ばれた回数を返す
print(m.method.call_count)