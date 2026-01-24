x = 2520
j = 1

while j <= 20:
    if x % j == 0:
        j += 1
    else:
        x += 1
        j = 1

print(x)

