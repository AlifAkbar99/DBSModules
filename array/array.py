import array

x = array.array("i",[1,2,3,4,5])
print(x)
print(type(x))

# list dalam array
print()
siswa = [90, 100, 50, 80, 85, 45, 80, 75, 50, 60]
print(siswa)
print(siswa[0])

# list dengan for
print()
var_arr = [0 for i in range(10)]
for i in range (10):
    var_arr[i] = i
print(var_arr)