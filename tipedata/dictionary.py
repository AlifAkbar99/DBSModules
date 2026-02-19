# Dictionary pada Python merupakan kumpulan pasangan key-value yang bersifat tidak berurutan

x = {'name': 'Muhammad Alif', 'age': 20, 'isMarried': False}
print(type(x))
print(x)
print(x['name'])

print()
# menambah data pada dictionary
x = {'name': 'Muhammad Alif', 'age': 20, 'isMarried': False}
x ['Job'] = 'AI Engineer'
print(x)

print()
# menghapus data pada dictionary
x = {'name': 'Muhammad Alif', 'age': 20, 'isMarried': False}
del x['isMarried']
print(x)

print()
# mengubah data pada dictionary
x = {'name': 'Muhammad Alif', 'age': 20, 'isMarried': False}
x['name'] = 'Jonrio Ebenezer'
print(x)