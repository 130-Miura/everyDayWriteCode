item_type = int(input())
items_price = list(map(int, input().split()))
money, orders = map(int, input().split())
for i in range(orders):
    item_type, quantity = map(int, input().split())
    order_price = items_price[item_type - 1] * quantity
    if money >= order_price:
        money -= order_price
print(money)