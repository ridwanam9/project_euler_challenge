
# i = 49
# # i = int(n)
# hasil = 0
# print(i, end="")
# count=1
# while hasil != 1:
#     if i%2 == 0:
#         hasil = i/2
#         i = hasil
#         print(f", {i}",end="")
#         count += 1
#     elif i%2 == 1:
#         hasil = i*3+1
#         i = hasil
#         print(f", {i}",end="")
#         count += 1

# print(f"\n jumlah = {count}")


longest_seq = 1
longest_start = 1
for i in range(500000, 1000000):
    n = i
    hasil = 0
    count=1
    while hasil != 1:
        if i%2 == 0:
            hasil = i/2
            i = hasil
            count += 1
        elif i%2 == 1:
            hasil = i*3+1
            i = hasil
            count += 1
    if count > longest_seq:
        longest_seq = count
        longest_start = n


print(f" Start = {longest_start}\n Jumlah Rantai = {longest_seq}")

    