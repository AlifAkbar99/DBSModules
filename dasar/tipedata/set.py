# Set adalah kumpulan item bersifat unik, tanpa urutan (unordered collection)
# Set tidak dapat indexing

x = {1, 2, 7, 2, 3, 13, 3}
print(x)
print(type(x))

print()
# union dan intersection
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

union = set1.union(set2)
print('Union: ', union)

intersection = set1.intersection(set2)
print('Intersection: ', intersection)