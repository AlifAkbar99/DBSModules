"""
TODO:
Buatlah sebuah fungsi bernama "minimal" dengan ketentuan berikut.
- Menerima dua buah argumen berupa number, yaitu a dan b.
- Mengembalikan nilai terkecil antara a atau b.
- Bila nilai keduanya sama, kembalikan dengan nilai a.
"""


def minimal(a,b):
    if a<=b :
        return a
    else:
        return b
nilai_kecil = minimal(3,4)
print(nilai_kecil)