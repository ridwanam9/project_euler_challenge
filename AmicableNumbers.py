

n = 7
# m = 5
print(f"n = {n}")
print("-------------")

p = 3*(2**(n-1)) - 1
print(p)
q = 3*(2**n) - 1
print(q)
r = 9*(2**(2*n-1)) - 1
print(r)


# p = ((2^(n-m)) + 1) * (2^m) - 1
# print(p)
# q = ((2^(n-m)) + 1) * (2^n) - 1
# print(q)
# r = ((2^(n-m)) + 1) * (2^(m + n)) - 1
# print(r)

print("-------------")

a = (2**n) * p * q
print(a)
b = (2**n) * r
print(b)

print("-------------")
sumA1 = 0
print(f"{a} Divisors = ", end="")
for j in range(1, a):
    if a%j == 0:
        print(j, end=" ")
        sumA1 += j
print(f"\n d({a}) = {sumA1}")

print("\n")
sumA2 = 0
print(f"{b} Divisors = ", end="")
for x in range(1, b):
    if b%x == 0:
        print(x, end=" ")
        sumA2 += x
print(f"\n d({b}) = {sumA2}")