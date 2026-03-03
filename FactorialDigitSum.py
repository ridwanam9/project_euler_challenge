def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1
  # Recursive case
  else:
    return n * factorial(n - 1)

facs = list(str(factorial(100)))

sum_digit = 0
for i in facs:
  t = int(i)
  sum_digit += t

print(sum_digit)