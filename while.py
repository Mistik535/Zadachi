n = int(input())
price = list(map(int, input().split()))

i = 0
s = 0
# while i < len(price):
#     print(price[i])
#     maximum = price[i]
#     for j in range(i+1, len(price)):
#         if price[j] > maximum:
#             maximum = price[j]
#     s += maximum
#     i += 1
i = n - 1
maximum = 0
while i >= 0:
    if price[i] > maximum:
        maximum = price[i]
    s += maximum
    i -= 1
print(s)
