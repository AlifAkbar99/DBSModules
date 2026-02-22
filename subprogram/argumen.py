"""
Keyword argument adalah jenis argumen yang disertai dengan nama 
parameter (identifier) dan secara eksplisit disebutkan.

def fungsi_saya(a,b,c):
fungsi_saya(1, b=50, c='Dicoding')
"""

def mencari_luas_persegi_panjang(panjang, lebar):
    luas_persegi_panjang = panjang * lebar
    return luas_persegi_panjang
persegi_panjang_pertama = mencari_luas_persegi_panjang(panjang = 5, lebar = 10)

print(persegi_panjang_pertama)