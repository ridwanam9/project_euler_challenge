

results = []

for x in range(100, 1000):
    for j in range(100, 1000):
        # print(f"{x} * {j} = {x*j}")
        results.append(str(x*j))
        

for result in results:
    if result == result[::-1]:
        print(result)







# x = range(100, 1000)
# print(list(x))