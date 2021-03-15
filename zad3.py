# Задача 3
# Отсортируйте словарь по значению в порядке возрастания и убывания.

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
list_d = list(d.items())
list_d.sort(key=lambda i: i[1])
print(list_d)

import operator
result = dict(sorted(d.items(), key=operator.itemgetter(1)))
print(result)

result = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
print(result)