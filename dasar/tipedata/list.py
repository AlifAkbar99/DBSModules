x = [1, 2.2, 'Dicoding']
print(type(x))
print()

# indexing
x = [1, 'Dicoding', True, 1.5]
print(x[2])
print()

# mutable
x = [1, 2.2, 'Dicoding']
x[0] = 'Indonesia'
print(x)
print()

# indexing plus mines
x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]
print(x[0])
print(x[2])
print(x[-1])
print(x[-3])
print()

# Konsep slicing. sequence[start:stop:step]

x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]
print(x[0:5:2])
print(x[1:])
print(x[:3])

