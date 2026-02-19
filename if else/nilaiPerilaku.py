nilai = 82
perilaku = 'Tidak baik'

if nilai>=80 and perilaku == 'baik':
    print("Selamat! anda mendapat nilai A dan telah berkelakukan baik")
    print("Pertahankan!")
elif nilai >= 80 and perilaku != 'baik':
    print("kamu mendapat nilai A, tapi tidak berkelakukan baik")
    print("Perbaikin lagi ya!")
else:
    print("Yuk belajar lebih giat lagi")