# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
#  (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль
#  (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и
# отдельно вывести наименования предприятий, чья прибыль ниже среднего.

# import collections
from collections import namedtuple
from collections import Counter

Company = namedtuple('Company', ['name', 'first_profit', 'second_profit', 'third_profit', 'fourth_profit'])
list_company = []

a = int(input('Введите кол-во предприятий.'))
for i in range(a):
    name = input(f'Введите наименование {i+1} - го предприятия: ')
    p_1 = int(input('Введите прибыль 1-го квартала= '))
    p_2 = int(input('Введите прибыль 2-го квартала= '))
    p_3 = int(input('Введите прибыль 3-го квартала= '))
    p_4 = int(input('Введите прибыль 4-го квартала= '))
    comp = Company(name, p_1, p_2, p_3, p_4)
    list_company.append(comp)

# print(list_company)
summ_av = 0
av_profit = {}
for i in range(len(list_company)):
    av_profit.setdefault(list_company[i].name, float((list_company[i].first_profit + list_company[i].second_profit + list_company[i].third_profit + list_company[i].fourth_profit) / 4))
    summ_av += av_profit[list_company[i].name]

print(f'Предприятия и их среднегодовая прибыль: {av_profit}')
av_summ = int(summ_av / len(av_profit))
print(f'Среднегодовая прибыль за год по отрасли =  {av_summ}')

list_below_av_summ = []
list_above_av_summ = []
list_equal_av_summ = []
for i in range(len(av_profit)):
    if av_profit[list_company[i].name] > av_summ:
        list_above_av_summ.append(list_company[i].name)
    elif av_profit[list_company[i].name] < av_summ:
        list_below_av_summ.append(list_company[i].name)
    else:
        list_equal_av_summ.append(list_company[i].name)


print(f'Предприятия, чья среднегодовая прибыль за год была выше среднего {list_above_av_summ}')
print(f'Предприятия, чья среднегодовая прибыль за год равна среднему показателю {list_equal_av_summ}')
print(f'Предприятия, чья среднегодовая прибыль за год была ниже среднего {list_below_av_summ}')