class Baju:
    def __init__(self, warna, merek, harga):
        self.warna = warna
        self.merek = merek
        self.harga = harga

baju_1 = Baju('Coklat', 'Ralph Lauren', 'Rp120000')
print(baju_1.warna)
print(baju_1.merek)
print(baju_1.harga)