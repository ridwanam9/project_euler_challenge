
# # versi sendiri
# longest_seq = 1
# longest_start = 1
# for i in range(500000, 1000000):
#     n = i
#     hasil = 0
#     count=1
#     while hasil != 1:
#         if i%2 == 0:
#             hasil = i/2
#             i = hasil
#             count += 1
#         elif i%2 == 1:
#             hasil = i*3+1
#             i = hasil
#             count += 1
#     if count > longest_seq:
#         longest_seq = count
#         longest_start = n


# print(f" Start = {longest_start}\n Jumlah Rantai = {longest_seq}")




# versi yang lebih optimal dan cepat dengan bantuan AI
cache = {1: 1}

longest_seq = 0
longest_start = 1

for i in range(1, 1_000_000):
    n = i
    steps = 0

    while n not in cache:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3*n + 1
        steps += 1

    total_length = steps + cache[n]
    cache[i] = total_length

    if total_length > longest_seq:
        longest_seq = total_length
        longest_start = i

print("Start =", longest_start)
print("Chain length =", longest_seq)
    