# pass
x = 10

if x > 5:
    pass
else:
    print("Nilai x tidak memenuhi kondisi")

print()
# list comprehension
angka = [1,2,3,4]
pangkat = []
for n in angka:
    pangkat.append(n**2)
print(pangkat)

print()
# list comprehension 2
angka = [1,2,3,4]
pangkat = [n**2 for n in angka]
print(pangkat)