# задание 3.1 

#О состояние программы можно сказать, что стек обращается к greet, потом обращается к greet2 и возвращает greet, который продолжает выполнение

# задание 3.2

# при бесконечной рекурсии будет выделятся стек пока не закончится а как только он закончится выдаст ошибку

# задание 1 

# def sum_iterative(x):
#     if x == 0:
#         return 0
#     else:
#         return x + sum_iterative(x-1)

# print(sum_iterative(5))


# задание 2 


# def factorial_iterative(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial_iterative(n-1)
# print(factorial_iterative(5)) 


# задание 3


# def fibonacci_iterative(n):
#     if n <= 0:
#         return 0
#     else:
#         return 1
#     return fibonacci_iterative(n - 1) + fibonacci_iterative(n - 2)


# print(fibonacci_iterative(7))  

# задание 4

# def power_iterative(base, exponent):
#     if exponent == 1:
#         return 1
#     return base * power_iterative(base, exponent - 1)
# print(power_iterative(2, 5))

# задание 5

# def print_reverse_iterative(n):
#     if n <= 1:
#         return 1
    
# print(n)
# print_reverse_iterative(n - 1)
