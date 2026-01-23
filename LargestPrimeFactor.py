def prime_factors(n):
    factors = []
    # Start with the first prime factor, 2
    i = 2
    while i * i <= n:
        # If 'i' divides 'n', add 'i' to the factors list and divide 'n' by 'i'
        if n % i == 0:
            factors.append(i)
            n //= i
        # Otherwise, increment 'i' to the next potential factor
        else:
            i += 1
    # If 'n' is greater than 1 after the loop, it is the remaining prime factor
    if n > 1:
        factors.append(n)
    return factors

# Example Usage:
number = 600851475143
result = prime_factors(number)
print(f"The prime factors of {number} are: {result}")
# Output: The prime factors of 315 are: [3, 3, 5, 7]
