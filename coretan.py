# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# thislist[4] = "grape"
# print(thislist)
# print(thislist[2:5])
# print(thislist[-4:-1])

#This will return the items from position 2 to 5.

#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included


import sys
sys.setrecursionlimit(10**6)
# print(sys.getrecursionlimit())


# def dfs(n):
#     if n == 0:
#         return 0
#     print(n, end=", ")
#     dfs(n-1)
# # print(dfs(5000))


# import time

# start = time.time()
# # Recursion Hitung Mundur
# def hitung_mundur(n):
#     if n == 0: return 0
#     print(n, end=", ")
#     return hitung_mundur(n-1)

# print("Recursion")
# print(hitung_mundur(998))
# end = time.time()
# print("Durasi:", end - start, "detik")

# print("--------------")


# start = time.time()
# # Looping Hitung Muundur
# print("Looping")
# for i in range(100, -1, -1):
#     print(i, end=", ")
# end = time.time()
# print("Durasi:", end - start, "detik")






target = 20
for i in range(10):
    for j in range(10):
        if i+j == target:
            print("True")
            break
        break
    
    # print("False")
    
