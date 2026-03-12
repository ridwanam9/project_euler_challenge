import itertools

# # Contoh 1: Permutasi 3 huruf dari string 'ABC'
# data = ['A', 'B', 'C']
# permutasi = list(itertools.permutations(data))
# print(permutasi)
# # Output: [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]

# # Contoh 2: Permutasi 2 objek dari 4 objek
# data2 = ['A', 'B', 'C', 'D']
# perms2 = list(itertools.permutations(data2, 2))
# print(perms2)
# # Output: [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'A'), ('B', 'C'), ('B', 'D'), ('C', 'A'), ('C', 'B'), ('C', 'D'), ('D', 'A'), ('D', 'B'), ('D', 'C')]


angka = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
perms = list(itertools.permutations(angka))
data_kesatujuta = "".join(perms[999999])
print(data_kesatujuta)