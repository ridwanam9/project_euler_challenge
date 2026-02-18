# Kita tahu: k * m * (m + n) = 500

target = 500

for m in range(2, int(target**0.5)):
    for n in range(1, m):
        if target % (m * (m + n)) == 0:
            k = target // (m * (m + n))
            
            a = k * (m**2 - n**2)
            b = k * (2 * m * n)
            c = k * (m**2 + n**2)
            
            if a + b + c == 1000:
                print("a, b, c =", a, b, c)
                print("abc =", a * b * c)
