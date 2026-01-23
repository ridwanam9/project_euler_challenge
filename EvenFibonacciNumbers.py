
# nilai fibo tidak melebihi 4 juta

fibonacci = []

a, b = 0, 1

while a <= 4000000:
    fibonacci.append(a)
    a, b = b, a+b

evens = []

for even_number in fibonacci:
    if even_number % 2 == 0:
        evens.append(even_number)

print(sum(evens))


################################


# # jumlah bilangan fibo tidak mencapai 4 juta

# fibo2 = []
# a, b = 0, 1

# for _ in range(4000000):
#     fibo2.append(a)
#     a, b = b, a+b

# evens = []

# for even_number in fibo2:
#     if even_number % 2 == 0:
#         evens.append(even_number)

# print(sum(evens))