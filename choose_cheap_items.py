# 割引率の違う商品のうち、最終価格が安い商品を出力する
# 割引率は10%以上で、10の倍数
# 定価は100円以上
# 割引後の金額が1円を下回ることはない

# 割引後の価格が安いほうの商品と割引後の金額を返す
# @return [商品名, 割引後の価格]
def choose_cheap_items(items):
    for i in range(0, len(items)):
        assert items[i][1] >= 100, '定価が100円を下回っています'
        assert items[i][2] >= 10, '割引率が10%を下回っています'
        assert items[i][2] % 10 == 0, '割引率が10の倍数になっていません'

        # 割引後の価格を計算
        price = int(items[i][1] * (100 - items[i][2]) / 100)
        assert price >= 1, '割引後の金額が1円を下回っています'

        # 安い方の商品の価格を代入
        if i == 0:
            temp_price = price
        else:
            if price < temp_price:
                temp_price = price
                
    return [items[i][0], temp_price]

# [商品名, 定価, 割引率]
items = [['チョコ', 100, 20], ['アイス', 100, 40]]
cheep_item = choose_cheap_items(items)
print(f'割引後の価格が{cheep_item[1]}円の{cheep_item[0]}が一番安い')