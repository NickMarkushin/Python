salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
for i in range(months, 1, -1):
    spend1 = spend
    for j in range(2, i + 1):
        spend1 = spend1 * (increase + 1)
    money_capital = money_capital + spend1 - salary
money_capital = money_capital + spend - salary
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(money_capital) + 1)
