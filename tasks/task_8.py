oklad = 50000  # рублей
tax_rate = 0.13  # 13% в десятичном виде

tax = oklad * tax_rate
salary = oklad - tax

print("Размер зарплаты:", oklad )
print("Размер подоходного налога:", tax)
print("Сумма на руки:", salary)
