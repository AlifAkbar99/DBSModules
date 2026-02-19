# contoh 1
count = 0

while count < 3:
    print("Dicoding Indonesia")
    count += 1
else:
    print("Blok else dieksekusi karena kondisi while salah")
    
print()

# contoh 2
n = 10
while n > 0:
    n = n - 1
    if n == 7:
        break
    print(n)
else:
    print('Loop selesai')
    