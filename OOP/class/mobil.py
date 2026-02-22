class Mobil:
    warna = 'Merah'

mobil_1 = Mobil()
mobil_1.warna = "Biru"
print(mobil_1.warna)

print()

class Motor:
    warna = "Merah"

motor_1 = Motor()
print(motor_1.warna)
motor_2 = Motor()
print(motor_2.warna)

Motor.warna = 'Hitam'

print(motor_1.warna)
print(motor_2.warna)