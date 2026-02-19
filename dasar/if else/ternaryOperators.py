lulus = True
print("selamat") if lulus else print("perbaiki")

print()

lulus = True
if lulus:
    print("Selamat")
else:
    print("Perbaiki")
    
print ()

lulus = True
kelulusan = ("Perbaiki, anda belum lulus.", "Selamat, anda lulus!")[lulus]
print(kelulusan)

print ()

lulus = True
if lulus:
    print("Selamat, Anda lulus!")
else:
    print("Perbaiki, Anda belum lulus!")