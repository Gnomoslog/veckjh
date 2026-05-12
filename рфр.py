# задание 1
# sau = int(input())
#
# berries = []
# for i in range(sau):
#     a = int(input())
#     berries.append(a)
#
# if sau == 1:
#     print(berries[0])
# elif sau == 2:
#     print(berries[0] + berries[1])
# else:
#     apl = 0
#     for i in range(sau):
#         s = berries[le] + berries[i] + berries[e]
#         if le < 0:
#             le = sau - 1
#
#         e = i + 1
#         if e >= sau:
#             e = 0
#
#         if s > apl:
#             apl = s
#
# print(apl)
#
from itertools import count

# задание 2

# n = int(input())
# c = [int(input()) for i in range(a)]
# m = int(input())
# g = [int(input()) for i in range(b)]
# asd = [x for x in c if x not in g]
### asd = set(c) - set(g) - не попорядку типа
# print(asd)

# задание 3
# c = int(input())
# a = list(map(int, input().split()))
# cot = 0
# for i in range(1, c - 1):
#     if a[i] > a[i - 1] and a[i] > a[i + 1]:
#         cot += 1
# print(cot)
# задание 4
# n = int(input("Введи размер массива:"))
# I = []
# if n <= 5:
#     print("")
# else:
#     for i in range(n):
#         v = int(input())
#         I.append(v)
# print(I)
#
# co = 0
# for h in range(n - 1):
#     if I[h] == I[h + 1]:
#         co += 1
#
# print(co)
#
