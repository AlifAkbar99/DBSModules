class Mobil:
    # Atribut instance
    def __init__(self):
        self.warna = "Kuning"
        
mobil_1 = Mobil()
mobil_2 = Mobil()
print(mobil_1.warna)
print(mobil_2.warna)

# mengubah warna

mobil_1.warna = "Hijau"
print(mobil_1.warna)
print(mobil_2.warna)