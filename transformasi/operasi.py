# len()
list = [1,3,5,7,9,11]
print(list)
print(len(list))

print()
# set()
list = set ([1,1,3,3,5,5,7,7,9,9,11,11])
print(list)
print(len(list))
contoh = 'Belajar Python'
print(len(contoh))

print()
# min dan max
angka = [11, 23, 45, 12, 8, 76, 198]
print(min(angka))
print(max(angka))

print()
# count()
genap = [2,4,6,6,6,8,10,12,14,16]
print(genap.count(6))
string = "rumahku besar sekali"
substring = 'a'
print(string.count(substring))

print()
# in and not in
kalimat = 'Belajar di Dicoding sangat menyenangkan'
print('Dicoding' in kalimat)
print('tidak' in kalimat)
print('Belajar' not in kalimat)
print('ayam' not in kalimat)

print()
# nilai multiple variable
data = ['shirt', 'white', 'L']
# apparel = data[0]
# color = data[1]
# size = data[2]
apparel, color, size = data
print(data)
print(apparel)
print(color)
print(size)

print()
# sort()
kendaraan = ['motor', 'mobil', 'becak']
kendaraan.sort()
print(kendaraan)

kendaraan = ['motor', 'mobil', 'becak']
kendaraan.sort(reverse=True)
print(kendaraan)