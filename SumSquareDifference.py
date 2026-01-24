sum_of_the_squares = []
square_of_the_sum = []

for x in range(1, 101):
    sum_of_the_squares.append(x**2)
    square_of_the_sum.append(x)


i = sum(sum_of_the_squares)
y = sum(square_of_the_sum)**2

# print(y)
# print(i)
print(y-i)
