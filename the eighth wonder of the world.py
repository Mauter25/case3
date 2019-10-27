year = 1
i = 1
years = int(input('Срок размещения капитала (лет):'))
start_capital = int(input('Начальный капитал ($):'))
interest = int(input('Процентная ставка (%/мес.):'))
investments = int(input('Инвестиционные вливания ($/мес.):'))
first_income = start_capital*(1+interest/100)
sum_of_percent = start_capital * interest/100
print(year, 'год')
print("-------------------------------------------")
print("|       |   основа   | сумма %  |         |")
print("| месяц | инвестиций | за месяц | капитал |")
print("-------------------------------------------")
print("|  ",i,"  |  "'{:.2f}'.format(first_income - sum_of_percent), "  |  "'{:.2f}'.format(sum_of_percent), "  | "'{:.2f}'.format(first_income), "|")
capital = first_income
for _ in range(11):
    capital += investments
    sum_of_percent = capital * interest / 100
    capital = capital * (1 + interest / 100)
    print("|  ",i + 1,"  |  "'{:.2f}'.format(capital - sum_of_percent), "  |  "'{:.2f}'.format(sum_of_percent), "  | "'{:.2f}'.format(capital), "|")
    i += 1
print("-------------------------------------------")
print()
for _ in range(years-1):
    year += 1
    print(year, 'год')
    print("-------------------------------------------")
    print("|       |   основа   | сумма %  |         |")
    print("| месяц | инвестиций | за месяц | капитал |")
    print("-------------------------------------------")
    i = 1
    for _ in range(12):
        capital += investments
        sum_of_percent = capital * interest / 100
        capital = capital * (1 + interest / 100)
        print("|  ",i + 1,"  |  "'{:.2f}'.format(capital - sum_of_percent), " |  "'{:.2f}'.format(sum_of_percent), "| "'{:.2f}'.format(capital), "|")
        i += 1
    print("-------------------------------------------")
    print()
