per_cent = {'ТКБ' : 5.6, 'СКБ' : 5.9, 'ВТБ' : 4.28, 'СБЕР' : 4.0}
money = input("Введите сумму первоначального взноса: ")
money = int(money)
percent_values = list(per_cent.values())
income = money*percent_values[0], money*percent_values[1], money*percent_values[2], money*percent_values[3]
income_int = list(map(int, income))
print(income_int)
print("Максимальная сумма, которую вы можете заработать - ", max(income_int))
