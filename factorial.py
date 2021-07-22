# def factorial(n):
#     pr=1
#     for i in range (2, n+1):
#         pr = pr * i
#     print(pr)
#
# factorial(6)

# palindrom

# def palindrom(s):
#     if len(s) <= 1:
#         return True
#     if s[0] != s[-1]:
#         return False
#     return palindrom(s[1:-1])
#
#
# print(palindrom("шалаш"))

a = [(x**3,y) for x in [3,5,7] for y in [1,2,3]]
print(a)
