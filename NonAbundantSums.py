

# # Menentukan bilangan abundant (True/False)
# bilangan = 30
# # print(type(bilangan))
# jumlah = 0
# for i in range(1, bilangan):
#     if bilangan%i == 0:
#         print(i, end=", ")
#         jumlah += i

# if jumlah > bilangan:
#     print(f"\n{jumlah} > {bilangan} = {True}")
# else:
#     print(f"\n{jumlah} > {bilangan} = {False}")



# import sys
# sys.setrecursionlimit(10**6)
# import logging

# logging.basicConfig(level=logging.INFO)


# Fungsi untuk menentukan apakah angka2 di 
# dalam list(numbers) bisa dijumlah kan menghasilkan angka target(n)
# def canSum(targetSum, numbers, memo=None):
#     if memo is None:
#         memo = {}

#     if targetSum in memo: 
#         return memo[targetSum]
#     if targetSum == 0: 
#         return True
#     if targetSum < 0: 
#         return False
    
#     for n in numbers:
#         remainder = targetSum - n
#         if canSum(remainder, numbers, memo) == True:
#             memo[targetSum] = True
#             return True

#     memo[targetSum] = False
#     return False

# print(canSum(7, [2, 3]))





LIMIT = 28123

# Step 1: menghitung jumlah proper divisor untuk setiap angka
div_sum = [0] * (LIMIT + 1)

for i in range(1, LIMIT // 2 + 1):
    for j in range(i * 2, LIMIT + 1, i):
        div_sum[j] += i


# Step 2: mencari abundant numbers
abundant = []

for i in range(12, LIMIT + 1):
    if div_sum[i] > i:
        abundant.append(i)


# Step 3: menandai angka yang bisa dibuat dari dua abundant numbers
can_be_written = [False] * (LIMIT + 1)

for i in range(len(abundant)):
    for j in range(i, len(abundant)):
        s = abundant[i] + abundant[j]

        if s <= LIMIT:
            can_be_written[s] = True
        else:
            break


# Step 4: menjumlahkan angka yang tidak bisa dibuat
result = 0

for i in range(1, LIMIT + 1):
    if not can_be_written[i]:
        result += i


print(result)