cost = 1000
discount = 20
quantity = 3

sum_without_discount = cost * quantity
total_cost = sum_without_discount - (sum_without_discount * discount / 100)

print("Стоимость вашего заказа:", total_cost, "рублей")
