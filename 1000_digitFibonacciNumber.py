# import sys
# sys.setrecursionlimit(10**6)
# def fibRec(n, memo):
#     if n <= 1:
#         return n

#     if memo[n] != -1:
#         return memo[n]

#     memo[n] = fibRec(n - 1, memo) + \
#               fibRec(n - 2, memo)
#     return memo[n]

# def fib(n):
#     memo = [-1] * (n + 1)
#     return fibRec(n, memo)

# n = 1
# # print(fib(n))
# # print(type(fib(n)))

# while len(list(str(fib(n)))) <= 1000:
#     # print(f"Bilangan Fibo ke-{n}")
#     # print(f"Bilangan Fibo = {fib(n)}")
#     if len(list(str(fib(n)))) == 1000:
#         break
#     n += 1
# print(n)




# versi singkat
a, b = 1, 1
index = 2

while len(str(b)) < 1000:
    a, b = b, a + b
    index += 1

print(index)