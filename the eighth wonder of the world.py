# Case-study №3
# Developers: Mauter A. (30%)
# Kuzmin E. (30%)
# Petrov V. (50%)
import rulocal as ru

year = 1
i = 1
years = int(input(ru.Term_of_capital_allocation))
start_capital = int(input(ru.Seed_capital))
interest = int(input(ru.Interest_rate))
investments = int(input(ru.Investment_injections))
first_income = start_capital * (1 + interest / 100)
sum_of_percent = start_capital * interest / 100
print(year, ru.year)
print("-------------------------------------------")
print(ru.base__amount_of_percent)
print(ru.month__investment__per_month__capital)
print("-------------------------------------------")
print("|  ", i, "  |  "'{:.2f}'.format(first_income - sum_of_percent), "  |  "'{:.2f}'.format(sum_of_percent),
      "  | "'{:.2f}'.format(first_income), "|")
capital = first_income
for _ in range(11):
    capital += investments
    sum_of_percent = capital * interest / 100
    capital = capital * (1 + interest / 100)
    print("|  ", i + 1, "  |  "'{:.2f}'.format(capital - sum_of_percent), "  |  "'{:.2f}'.format(sum_of_percent),
          "  | "'{:.2f}'.format(capital), "|")
    i += 1
print("-------------------------------------------")
print()
for _ in range(years - 1):
    year += 1
    print(year, ru.year)
    print("-------------------------------------------")
    print(ru.base__amount_of_percent)
    print(ru.month__investment__per_month__capital)
    print("-------------------------------------------")
    i = 1
    for _ in range(12):
        capital += investments
        sum_of_percent = capital * interest / 100
        capital = capital * (1 + interest / 100)
        print("|  ", i + 1, "  |  "'{:.2f}'.format(capital - sum_of_percent), " |  "'{:.2f}'.format(sum_of_percent),
              "| "'{:.2f}'.format(capital), "|")
        i += 1
    print("-------------------------------------------")
    print()
