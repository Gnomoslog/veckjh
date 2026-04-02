# задание 1


# задание  2

li = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
max = int(input())
min = int(input())

ind = []

for i in range(len(li)):
    if min <= li >= max:
        ind.append(i)
print(li)