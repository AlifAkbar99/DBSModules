for i in range(2):
    print("Perulangan luar: ", i)
    for j in range(10):
        print("Perulangan dalam: ", j)
        if j == 1:
            break # menghentikan perulangan dalam jika j = 1

print()

for huruf in 'Dico ding':
    if huruf == ' ':
        break
    print("Huruf saat ini: {}".format(huruf))