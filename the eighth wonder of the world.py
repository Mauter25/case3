# Case-study №3
# Developers: Mauter A. (30%)
# Kuzmin E. (30%)
# Petrov V. (50%)
import rulocal as ru

year = 1
i = 1
years = int(input(ru.Term_of_capital_allocation))    #how many years do you want to keep a contribution.
start_capital = int(input(ru.Seed_capital))          #your primery contribution.
interest = int(input(ru.Interest_rate))              #which percent do you want to take.
investments = int(input(ru.Investment_injections))   #your followings investments
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
for _ in range(11):                                 #it makes easier to see, how your capital is growing every mounth.
    capital += investments                          #the tables which means years and the strings which means the mounth.
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
