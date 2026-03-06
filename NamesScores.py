with open("names.txt") as f:
    names = f.read().replace('"', '').split(',')

names.sort()

total = 0

for i, name in enumerate(names, start=1):
    value = sum(ord(c) - 64 for c in name)
    total += value * i

print(total)