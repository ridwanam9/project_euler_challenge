
import math

def count_divisors(n):
    count = 1
    temp = n
    i = 2
    
    while i * i <= temp:
        exponent = 0
        while temp % i == 0:
            temp //= i
            exponent += 1
        if exponent > 0:
            count *= (exponent + 1)
        i += 1
    
    if temp > 1:
        count *= 2
        
    return count

def first_triangle_with_divisors(limit):
    n = 1
    triangle = 1
    
    while True:
        if count_divisors(triangle) > limit:
            return triangle
        n += 1
        triangle += n

print(first_triangle_with_divisors(500))