# Задача 5
# Найдите три ключа с самыми высокими значениями в словаре

my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}

result = sorted(my_dict, key=my_dict.get, reverse=True)[:4]
print(result)

from heapq import nlargest
result = nlargest(3, my_dict, key=my_dict.get)
print(result)