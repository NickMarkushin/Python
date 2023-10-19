money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
total = money_capital + salary
s = 0
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while total > spend:
    total -= spend
    total += salary
    s += 1
    spend *= (increase + 1)
print("Количество месяцев, которое можно протянуть без долгов:", s)
